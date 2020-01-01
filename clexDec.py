import base64

def clexDec(readFile, writeFile):
    with open(readFile, 'rb') as inFile:
        editStr = base64.b64decode(inFile.read())
    with open(writeFile, 'wb') as outFile:
        outFile.write(editStr)
    print('Image saved in ' + writeFile)