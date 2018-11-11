from hashlib import sha1
from Crypto.Cipher import DES3
from Crypto.PublicKey import RSA
from Crypto import Random

# Path of output file
output_file_path = '../cipher.txt'
# Path of file holding Initialization vector
iv_file_path = '../iv.txt'
# Path of Public key
pk_file_path = '../public_key.pem'
# Path of Public key
enc_key_file_path = '../enc_key.txt'

#============== Plain Text ===========================
# get path of the plain text
plain_text_path = input('\n\n** Enter Plain Text File Path:  ')

# plain text data
plain_text = ''
# read the plain text file to get the plain text data
with open(plain_text_path, 'r') as plainTextFile:
  plain_text = plainTextFile.read()

# Add padding to plain text
l = len(plain_text)
if l % 8 != 0:
    toAdd = 8 - l % 8
    for i in range(toAdd):
      plain_text += ' '
      
#============ SHA-1 ================================

# get sha-1 result for the plain text data
sha1_plain_text = sha1(plain_text.encode('utf-8')).hexdigest()
print('==> SHA1 Result: ' + sha1_plain_text)

# Add sha1 result to the output file
with open(output_file_path, "w") as outputFile:
    outputFile.write(sha1_plain_text)
    outputFile.write('\n')

#============= RSA + 3-DES ================================
# 16 byte random key
key = Random.get_random_bytes(16)

#======== RSA ==========
public_key = ''
# Read public key
with open(pk_file_path, "r") as pkFile:
    public_key = pkFile.read()
public_key_obj =  RSA.importKey(public_key)
# encrypt the key 
enc_key = public_key_obj.encrypt(key, 32)[0]
# Add encrypted key to new file
with open(enc_key_file_path, "wb") as outputFile:
    outputFile.write(enc_key)
# print Encrypted key
print('\n\n==> Encrypted Key for 3-DES:')
with open(enc_key_file_path, "rb") as inputFile:
    print(inputFile.read())

#======== 3-DES ==========
# Initialization vector for DES
iv = Random.new().read(DES3.block_size)

# Block Cipher Mode CBC (Cipher-Block Chaining) 
cipher = DES3.new(key, DES3.MODE_CBC, iv)

# Add padding to plain text
# l = len(plain_text)
# if l % 8 != 0:
#     toAdd = 8 - l % 8
#     for i in range(toAdd):
#       plain_text += ' '
# get cipher text
cipher_text = cipher.encrypt(str.encode(plain_text))

# Add cipher to the end of output file
with open(output_file_path, "ab") as outputFile:
    outputFile.write(cipher_text)
# print cipher text
print('\n\n==> SHA1 + Cipher Text:')
with open(output_file_path, "rb") as inputFile:
    print(inputFile.read())

# Add initialization vector to a file
with open(iv_file_path, "wb") as ivFile:
    ivFile.write(iv)

# print files 
print('\n\n== Cipher Text with SHA-1 hash File in: ' + output_file_path)
print('== Encrypted 3-DES key in: ' + enc_key_file_path)
print('== Initialization vector for 3-DES key in: ' + iv_file_path)
print('\n\n')