#!/usr/bin/env python3

# imports
import base64
import sys

def textImage():    
    fileName = input('Input path of the text file: ')       # user inputs text file path
    # program reads the text file
    with open(fileName, 'rb') as textFile:
        imageStr = textFile.read()
    # decoding text
    imageStr = base64.b64decode(imageStr)
            
    # user inputs path to the new image file
    dirPath = input('Input the name of the new image file: ')
    if not '.' in dirPath:                                  # program checks for file extension
        ext = input('Please input file extension: ')
        if not '.' in ext:
            print('ERROR: This is not a correct file extension. Exiting...')
            sys.exit()

        # adding file extension to dirPath
        dirPath = dirPath + ext
        
    # writing converted string to image file
    with open(dirPath, 'wb') as imageFile:
        imageFile.write(imageStr)
        imageFile.close()

    print('Operation completed successfully!')
    print('File saved in ' + dirPath)