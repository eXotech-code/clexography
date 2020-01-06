# compression function
def compress(startFile):
    with open(startFile, 'r') as textFile:                # program opens startFile as a string
        startStr = textFile.read()

    print('startStr:\n' + startStr[0:100])

    repeats = ''
    count = 1

    repeats += startStr[0]

    for i in range(len(startStr)-1):
        if(startStr[i] == startStr[i+1]):
            count += 1
        else:
            if(count > 1):
                repeats += str(count)
            repeats += startStr[i+1]
            count = 1
    if(count > 1):
        repeats += str(count)

    print('repeats:\n' + repeats[0:100])

    startFile = 'compressed-' + startFile

    with open(startFile, 'w') as outFile:
        outFile.write(repeats)
    print('Text file saved as ' + startFile)
    
startFile = input('[DEV] Input startFile: ')
compress(startFile)