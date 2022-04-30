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

    NewFileName = ''.join(random.choices(string.ascii_letters +  string.digits, k=OldFileNameLen))
    NewExtension = ''.join(random.choices(string.ascii_letters +  string.digits, k=OldExtensionLen))
    NewFilePath = OldFilePath.rsplit('\\', 1)[0] + "\\" + NewFileName + "." + NewExtension
    
    os.rename(dst=NewFilePath, src=OldFilePath)
    os.remove(NewFilePath)
