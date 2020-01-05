import collections

# compression function
def compress(startFile, finalFile):
    with open(startFile, 'r') as inFile:                # program opens startFile as a string
        startStr = inFile.read()

    finalStr = collections.Counter(startStr)
    print(finalStr)

startFile = 'test.txt'
finalFile = 'compressed.txt'
compress(startFile, finalFile)