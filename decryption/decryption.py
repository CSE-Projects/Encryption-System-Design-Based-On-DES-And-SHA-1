from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5

# Read ciphertext
read_cipher = open("../output.txt","r")
cipher_text = read_cipher.read() 

# Read private key 
keyPriv = RSA.importKey("private_key.pem") 
cipher = Cipher_PKCS1_v1_5.new(keyPriv)

# Decrypt text
decrypt_text = cipher.decrypt(cipher_text, None).decode()

# DES decryption

# Hash calculation

# Verification

# Printing
