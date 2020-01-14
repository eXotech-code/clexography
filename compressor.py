# compression function
def compress(startStr):

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
    return repeats

def decompress(repeats):
    if any(char.isdigit() for char in repeats):
        print('Yeah boy')
    else:
        return repeats
    
startStr = input('[DEV] Input startStr: ')
decompress(compress(startStr))