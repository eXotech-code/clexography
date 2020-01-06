import re

# compression function
def compress(startFile):
    with open(startFile, 'r') as textFile:                # program opens startFile as a string
        startStr = textFile.read()

    print('startStr:\n' + startStr[0:100])

    repeats = re.sub(r'[^\w\s]|(.)(?=\1)', '', startStr)

    print('repeats:\n' + repeats[0:100])

    startFile = 'compressed-' + startFile

    with open(startFile, 'w') as outFile:
        outFile.write(repeats)
    print('Text file saved as ' + startFile)
    
startFile = input('[DEV] Input startFile: ')
compress(startFile)