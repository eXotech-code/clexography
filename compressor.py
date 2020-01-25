import re

# compressor
def compress(startStr):
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

# decompressor
def decompress(repeats):
    while any(char.isdigit() for char in repeats):
        match = re.match(r"([a-z]+)([0-9]+)", repeats, re.I)
        groupReplace = repeats.replace(match.group(1) + match.group(2), '')
        print(groupReplace)
        repeats = match.group(1) * int(match.group(2)) + groupReplace
        print(repeats)
    
startStr = input('[DEV] Input startStr: ')
decompress(compress(startStr))