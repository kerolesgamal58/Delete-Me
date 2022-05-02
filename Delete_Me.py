# This tool is used to delete any file from disk and make it impossible to recover it again
# First we open the file and write on it n bytes of null byte 0x00
# and rename the file (using random alphanumeric characters) to delete any artifact about filename

# note: we could recover the filename from $I30 index entry on ntfs
# this entry exists in every directory and contains index of all files/directories that belong to this directory

import os
import random
import string
import sys


OldFilePath = sys.argv[1]

if not os.path.isfile(OldFilePath):
    print ("File not exist")
    exit
else:
    FileSize = os.path.getsize(OldFilePath)

    file = open(OldFilePath, "bw")
    file.write(b'\x00' * FileSize)
    file.close()

    OldFileName = OldFilePath.rsplit('\\', 1)[-1]
    OldFileNameLen = len(OldFileName.rsplit('.', 1)[0])
    OldExtensionLen = len(OldFileName.rsplit('.', 1)[-1])

    # Generate a new name with random alphanumeric characters with the same original length
    NewFileName = ''.join(random.choices(string.ascii_letters +  string.digits, k=OldFileNameLen))
    NewExtension = ''.join(random.choices(string.ascii_letters +  string.digits, k=OldExtensionLen))
    NewFilePath = OldFilePath.rsplit('\\', 1)[0] + "\\" + NewFileName + "." + NewExtension
    
    os.rename(dst=NewFilePath, src=OldFilePath)
    os.remove(NewFilePath)
