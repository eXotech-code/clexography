import re

# transforming list into string
def listToString(repeatsCut):
    finalStr = ''
    for ele in repeatsCut:
        finalStr += ele
    return finalStr

    

# compression function
def compress(startFile, finalFile):
    with open(startFile, 'r') as inFile:                # program opens startFile as a string
        startStr = inFile.read()

    repeats = re.findall(r'((.)\2*)', startStr)
    # it this stage i have [('111', '1'), ('2', '2'), ('3', '3'), ('4', '4')] in l

    # now I am keeping only the first value from the tuple of each list
    repeatsCut = [x[0] for x in repeats]

    print(repeatsCut)

    finalStr = listToString(repeatsCut)

    with open(finalFile, 'w') as outFile:
        outFile.write(finalStr)

startFile = 'test.txt'
finalFile = 'compressed.txt'
compress(startFile, finalFile)