from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Crypto.Cipher import DES3
from hashlib import sha1
import sys

#============ RSA ================================

# Path of encrypted DES keys
read_cipher = open("../enc_key.txt","rb")

# Reading encrypted keys
cipher_text = read_cipher.read() 

# Importing RSA private keys 
private_key = ''
with open('private_key.pem', "r") as skFile:
    private_key = skFile.read()
keyPriv = RSA.importKey(private_key) 

#============ 3-DES ================================

# Decrypting DES_key
DES_key = keyPriv.decrypt(cipher_text)
print('\n\n==> DES key: ')
sys.stdout.buffer.write(DES_key)

# Reading IV 
with open('../iv.txt', "rb") as ivFile:
    iv = ivFile.read()
print('\n\n==> Initial Vector: ')
sys.stdout.buffer.write(iv)

#============ SHA-1 ================================

with open('../cipher.txt', "rb") as cipherFile:
    hash_value = cipherFile.readline()
    encrypted_text = cipherFile.read()
cipher_decrypt = DES3.new(DES_key, DES3.MODE_CBC, iv)
deciphered_text = cipher_decrypt.decrypt(encrypted_text)
deciphered_text = deciphered_text.decode("utf-8")
print('\n\n==> SHA-1 value: ')
sys.stdout.buffer.write(hash_value)

#============ SHA-1 ================================

# Authentication
sha1_plain_text = sha1(deciphered_text.encode('utf-8')).hexdigest()
if sha1_plain_text == hash_value.decode("utf-8").rstrip():
    print("\n\n\n#============ Success ================================")
    print(deciphered_text)
    deciphered_text.rstrip()
    with open("message.txt", "w") as outputFile:
        outputFile.write(deciphered_text)
else: 
    print("ERROR: Adversary tampering detected")