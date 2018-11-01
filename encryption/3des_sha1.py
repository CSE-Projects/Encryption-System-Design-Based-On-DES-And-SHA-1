from hashlib import sha1
from Crypto.Cipher import DES3
from Crypto import Random

# Path of output file
output_file_path = '../cipher.txt'
# Path of file holding Initialization vector
iv_file_path = '../iv.txt'

#============== Plain Text ===========================
# get path of the plain text
plain_text_path = input('\n\n** Enter Plain Text File Path:  ')

# plain text data
plain_text = ''
# read the plain text file to get the plain text data
with open(plain_text_path, 'r') as plainTextFile:
  plain_text = plainTextFile.read()

#============ SHA-1 ================================

# get sha-1 result for the plain text data
sha1_plain_text = sha1(plain_text.encode('utf-8')).hexdigest()
print('==> SHA1 Result: ' + sha1_plain_text)

# Add sha1 result to the output file
with open(output_file_path, "a") as outputFile:
    outputFile.write(sha1_plain_text)

#============= 3-DES ================================
# 16 byte random key
key = Random.get_random_bytes(16)

# Initialization vector for DES
iv = Random.new().read(DES3.block_size)

# Block Cipher Mode CBC (Cipher-Block Chaining) 
cipher = DES3.new(key, DES3.MODE_CBC, iv)

# Add padding to plain text
l = len(plain_text)
if l % 8 != 0:
    toAdd = 8 - l % 8
    for i in range(toAdd):
      plain_text += '0'
# get cipher text
cipher_text = cipher.encrypt(str.encode(plain_text))

# Add cipher to the end of output file
with open(output_file_path, "ab") as outputFile:
    outputFile.write(cipher_text)
# print cipher text
print('\n\n==> SHA1 + Cipher Text:')
with open(output_file_path, "rb") as outputFile:
    print(outputFile.read())

# Add initialization vector to a file
with open(iv_file_path, "ab") as ivFile:
    ivFile.write(iv)
print('\n\n== Cipher Text with SHA-1 hash File at: ' + output_file_path)