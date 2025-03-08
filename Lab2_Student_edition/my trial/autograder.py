from feistel import feistel
import sp
import json

with open ("testcases.json", 'r') as f:
    testcases = json.load(f)
    
OverallGrade = 5

def testRound():
    global OverallGrade
    num_completed, num_failed = 0, 0
    failed_flg = False
    print(f"\n\n---------------------------------------------------------------\nAUTOGRADER: testing Round function...")
    for i in range (len(testcases['testcases'])):
        L_r1 = testcases['testcases'][i]["L_r1"]
        R_r1 = testcases['testcases'][i]["R_r1"]
        Subkey = testcases['testcases'][i]["Subkey"]
        expected_round_L = testcases['testcases'][i]["expected_round_L"]
        expected_round_R = testcases['testcases'][i]["expected_round_R"]
        key = testcases['testcases'][i]["key"]
        testfeistel = feistel(key, sp.SP_Network, 2)
        L_block_next, R_block_next = testfeistel.round(L_block=L_r1, R_block= R_r1, subkey=Subkey)

        try:
            if(L_block_next == expected_round_L and expected_round_R == R_block_next):
                print(f"Test {i+1}  Completed")
                num_completed += 1
            else:
                print(f"Test {i+1}  Failed when Lblock={L_r1} and Rblock= {R_r1} while you output Lnext= {L_block_next} and Rnext= {R_block_next}")
                num_failed += 1
        except:
            print(f"AUTOGRADER: Error in testRound function")
            OverallGrade -= 1.0
            failed_flg = True
    
    if(not failed_flg):
        print(f"AUTOGRADER: Round function finished at {num_completed} out of {len(testcases['testcases'])}")
        OverallGrade -= num_failed*1/len(testcases['testcases'])


def testKeyScheduler():
    global OverallGrade
    num_completed, num_failed = 0, 0
    failed_flg = False
    print(f"\n\n---------------------------------------------------------------\nAUTOGRADER: testing keyScheduler function...")
    for i in range (len(testcases['testcases'])):
        key = testcases['testcases'][i]["key"]
        num_rounds = testcases['testcases'][i].get("num_rounds", 120)
        expected_subkeys = testcases['testcases'][i].get("expected_subkeys", [])
        testfeistel = feistel(key, sp.SP_Network, num_rounds)
        
        subkeys = testfeistel.keyScheduler()
        
        try:
            if([i in expected_subkeys for i in subkeys]):
                print(f"Test {i+1}  Completed")
                num_completed += 1
            else:
                print(f"Test {i+1}  Failed when key= {bin(key)[2:]} and num_rounds= {num_rounds}, expected: {[bin(i)[2:] for i in expected_subkeys]}")
                num_failed += 1
        except:
            print(f"AUTOGRADER: Error in testKeyScheduler function")
            OverallGrade -= 2.0
            failed_flg = True
    
    if(not failed_flg):
        print(f"AUTOGRADER: keyScheduler function finished at {num_completed} out of {len(testcases['testcases'])}")
        OverallGrade -= num_failed*2/len(testcases['testcases'])

def testFeistel():
    global OverallGrade
    num_completed, num_failed = 0, 0
    failed_flg = False
    print(f"\n\n---------------------------------------------------------------\nAUTOGRADER: testing Feistel network function...")
    for i in range (len(testcases['testcases'])):
        key = testcases['testcases'][i]["key"]
        message = testcases['testcases'][i].get("message", "lol")
        num_rounds = testcases['testcases'][i].get("num_rounds", 120)
        expected_CT = testcases['testcases'][i].get("expected_CT", "01010111")
        testfeistel = feistel(key, sp.SP_Network, num_rounds)
        Ct = testfeistel.feistel_network(message=message, encrypt_flag=1)

        try:
            if(expected_CT == Ct):
                print(f"Test {i+1}  Encryption Completed")
                num_completed += 1
            else:
                print(f"Test {i+1}  Encryption Failed when key= {key} and message= {message} while expected CT= {expected_CT}")
                num_failed += 1
        except:
            print(f"AUTOGRADER: Error in testFeistel encryption function")
            OverallGrade -= 2.0
            failed_flg = True
        
        if(not failed_flg):
            try:
                Pt = testfeistel.feistel_network(message=Ct, encrypt_flag=0)
                Pt = int(Pt, 2)
                if(Pt == message):
                    print(f"Test {i+1}  Decryption Completed")
                    num_completed += 1
                else:
                    print(f"Test {i+1}  Decryption Failed when key= {key} and message= {message} while the decrypted Pt= {Pt}")
                    num_failed += 1
            except:
                print(f"AUTOGRADER: Error in testFeistel decryption function")
                OverallGrade -= 2.0
                failed_flg = True
    if(not failed_flg):
        print(f"AUTOGRADER: Feistel network function finished at {num_completed} out of {len(testcases['testcases']) * 2}")
        OverallGrade -= num_failed*1/len(testcases['testcases'])
    
    
def Grade():
    global OverallGrade
    
    testKeyScheduler()
    testRound()
    
    try:
        testFeistel()
    except:
        print(f"AUTOGRADER: Error in testFeistel function")
        OverallGrade -= 2.0
    print(f"\n\n######################################\n#  AUTOGRADER: Final grade: {OverallGrade}/5.0  #\n######################################\n")






if __name__ == "__main__":    
    Grade()
    key= 1342135
    message = 1354544352
    print(f"Plaintext before encryption: {message : >40}")
    feistelObj = feistel(key, sp.SP_Network, 16)
    Ct = feistelObj.feistel_network(message=message, encrypt_flag=1)
    CipherText = int(Ct, 2)
    print(f"Ciphertext: {CipherText: >57}")
    
    
    Pt = feistelObj.feistel_network(message=Ct, encrypt_flag=0)
    Plaintext = int(Pt, 2)
    print(f"Plaintext after decryption:  {Plaintext: >40}")