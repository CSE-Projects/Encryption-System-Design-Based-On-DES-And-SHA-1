import os
from hashlib import sha1

# Path of output file
output_file_path = '../output.txt'

# get path of the plain text
plain_text_path = input('\n** Enter Plain Text File Path:  ')

# plain text data
plain_text = ''
# read the plain text file to get the plain text data
with open(plain_text_path, 'r') as plainTextFile:
  plain_text = plainTextFile.read()

# get sha-1 result for the plain text data
sha1_plain_text = sha1(plain_text.encode('utf-8')).hexdigest()
print('==> SHA1 Result: ' + sha1_plain_text)

# Add sha1 result to the end of output file
with open(output_file_path, "a") as outputFile:
    outputFile.write(sha1_plain_text)
