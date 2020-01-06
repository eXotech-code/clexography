# extension checker
def extCheck(sys, writeFile):
    if not '.' in writeFile:
        extChoice = input('Do you want to save this file with no extension? (Y/n): ').lower()
        if extChoice in ['n', 'no']:
            ext = input('Please input file extension: ')
            if not '.' in ext:
                print('ERROR: This is not a correct file extension. Exiting...')
                sys.exit()
            writeFile = writeFile + ext
            return writeFile                                                        # writeFile with extension
    # if extension checker finds extension, it returns unchanged writeFile string
    else:
        return writeFile

# encoder
def txtEncode(base64, readFile, writeFile):
    with open(readFile, 'rb') as inFile:
        editStr = base64.b64encode(inFile.read())
    with open(writeFile, 'wb') as outFile:
        outFile.write(editStr)
    print('Text file saved as ' + writeFile)

# decoder
def txtDecode(base64, readFile, writeFile):
    with open(readFile, 'rb') as inFile:
        editStr = base64.b64decode(inFile.read())
    with open(writeFile, 'wb') as outFile:
        outFile.write(editStr)
    print('Image saved as ' + writeFile)