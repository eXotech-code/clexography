#!/usr/bin/env python3

# imports
import base64
import sys

def imageText():
    # user specifies the file path
    filePath = input('Input path of the image file: ')
    # extension checker
    if not '.' in filePath:
        imgExt = input('Please input file extension: ')
        if not '.' in imgExt:
            print('ERROR: This is not a correct file extension. Exiting...')
            sys.exit()
        filePath = filePath + imgExt
    
    # converter
    with open(filePath, 'rb') as imageFile:
        imagestr = base64.b64encode(imageFile.read())   # decodes image raw data into string
        print(imagestr)                                 # prints the text from image data
    # saving as text file
    confirm = input('Do you want to save this as a text file? (Y/n): ').lower()
    if confirm in ['y', 'yes']:
        savePath = input('Input the name of the new text file: ')
        # extension checker
        if not '.' in savePath:
            extChoice = input('Do you want to save this file with no extension? (Y/n): ').lower()
            if extChoice in ['n', 'no']:
                ext = input('Please input file extension: ')
                if not '.' in ext:
                    print('ERROR: This is not a correct file extension. Exiting...')
                    sys.exit()
                savePath = savePath + ext
        text_file = open(savePath, 'wb')                            # opens the specified file name for editing
        text_file.write(imagestr)                                   # inserts image string to the text file
        text_file.close()
        print('Text file has been saved as: ' + (savePath))         # prints saved file's name
    elif confirm in ['n', 'no']:
        print('Text file has not been saved.')
    else:
        rerun = input('ERROR: function "' + (confirm) + '" is not a valid function. Do you want to run again? (Y/n): ').lower()
        if rerun in ['y', 'yes']:
            imageText()
        else:
            print('Exiting...')