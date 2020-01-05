import base64

def txtEncode(readFile, writeFile):
    with open(readFile, 'rb') as inFile:
        editStr = base64.b64encode(inFile.read())
    with open(writeFile, 'wb') as outFile:
        outFile.write(editStr)
    print('Text file saved in ' + writeFile)