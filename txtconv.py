#!/usr/bin/env python3

# imports
import base64
import sys

def textImage():    
    fileName = input('Input path of the text file: ')   # user inputs text file path
    # program reads the text file
    with open(fileName, 'rb') as textFile:
        imageStr = textFile.read()
    # converting bytes to utf-8
    imageStr = base64.b64decode(imageStr)
            
    # user inputs path to the new image file
    dirPath = input('Input the name of the new image file: ')
    if '.' in dirPath:                                  # program checks for file extension
        # writing converted string to image file
        with open(dirPath, 'wb') as imageFile:
            imageFile.write(imageStr)
            imageFile.close()

        print('Operation completed successfully!')
        print('File saved in ' + dirPath)
    else:
        ext = input('Please input file extension: ')
        if '.' in ext:
            # writing converted string to image file with file extension
            with open(dirPath + ext, 'wb') as imageFile:
                imageFile.write(imageStr)
                imageFile.close()

            print('Operation completed successfully!')
            print('File saved in ' + dirPath + ext)
        else:
            print('ERROR: This is not a corret file extension. Exiting...')
            sys.exit()