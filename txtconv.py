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
            
    # user inputs directory to which the converted image file will be saved
    dirPath = input('Input the name of the new image file (same extension as original): ')
            
    # writing converted string to image file
    with open(dirPath, 'wb') as imageFile:        # path to the file is predetermined (will change in the future)
        imageFile.write(imageStr)
        imageFile.close()
            
    print('Operation completed successfully!')
    print('File saved in ' + dirPath)