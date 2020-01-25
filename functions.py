# extension checker
def addExt(sys, writeFile):
    extChoice = input('Do you want to save this file with no extension? (Y/n): ').lower()
    if extChoice in ['n', 'no']:
        ext = input('Please input file extension: ')
        if not '.' in ext:
            print('ERROR: This is not a correct file extension. Exiting...')
            sys.exit()
        writeFile = writeFile + ext
        return writeFile                # writeFile with extension
    else:
        return writeFile                # If user wants to save file with no extension, extension checker returns unchanged writeFile string

def extCheck(sys, writeFile):
    if not '.' in writeFile:
        return addExt(sys, writeFile)
    elif writeFile[0] == '.':           # for when user wants to write file to current directory
        return addExt(sys, writeFile)
    # if extension checker finds extension, it returns unchanged writeFile string
    else:
        return writeFile

# file duplicate finder
def duplicateFinder(os, writeFile):
    if os.path.isfile(writeFile):
        filename, extension = os.path.splitext(writeFile)   # get extension
        writeFile = writeFile.replace(extension, '')
        writeFile = filename + '1'                          # add a number to filename
        # if that file exists as well iterate through all possible numbers
        # and if that name doesn't exist add that number to it and add it to writeFile.
        while os.path.isfile(writeFile):
            number = int(writeFile[-1]) + 1
            writeFile = writeFile.replace(writeFile[-1], str(number)) + extension
        return writeFile
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