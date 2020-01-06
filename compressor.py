import re

# compression function
def compress(startFile):
    with open(startFile, 'r') as textFile:                # program opens startFile as a string
        startStr = textFile.read()

    repeats = re.findall(r'((.)\2*)', startStr)
    repeatsCut = [x[0] for x in repeats]

    print(repeatsCut[0:100])

startFile = input('[DEV] Input startFile: ')
compress(startFile)