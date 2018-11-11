from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Crypto.Cipher import DES3
from hashlib import sha1

# Read DES keys
read_cipher = open("../enc_key.txt","rb")
cipher_text = read_cipher.read() 

# Decrypt DES keys 
private_key = ''
with open('private_key.pem', "r") as skFile:
    private_key = skFile.read()
keyPriv = RSA.importKey(private_key) 
DES_key = keyPriv.decrypt(cipher_text)

# Decrypt cipher.txt
with open('../iv.txt', "rb") as ivFile:
    iv = ivFile.read()

with open('../cipher.txt', "rb") as cipherFile:
    hash_value = cipherFile.readline()
    encrypted_text = cipherFile.read()
cipher_decrypt = DES3.new(DES_key, DES3.MODE_CBC, iv)
deciphered_text = cipher_decrypt.decrypt(encrypted_text)
deciphered_text = deciphered_text.decode("utf-8")

# Verification
sha1_plain_text = sha1(deciphered_text.encode('utf-8')).hexdigest()
if sha1_plain_text == hash_value.decode("utf-8").rstrip():
    deciphered_text.rstrip()
    with open("message.txt", "w") as outputFile:
        outputFile.write(deciphered_text)
else: 
    print("ERROR: Adversary tampering detected")