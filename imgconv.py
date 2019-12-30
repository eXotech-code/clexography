#!/usr/bin/env python3

# imports
import base64

def imageText():
    # user specifies the file path
    filePath = input('Input path of the image file: ')
    
    # converter
    with open(filePath, 'rb') as imageFile:
        imagestr = base64.b64encode(imageFile.read())   # decodes image raw data into string
        print(imagestr)                                 # prints the text from image data
    # saving as text file
    def imgAction():
        selectAction = input('Do you want to save this text as .txt file? (Y/n): ').lower()
        if rerun in ['y', 'yes']:
            savePath = input('Input the name of the new text file: ') + '.txt'
            text_file = open(savePath, 'wb')                            # opens the specified file name for editing
            n = text_file.write(imagestr)                               # inserts image string to the text file
            text_file.close()
            print('Text file has been saved as: ' + (savePath))         # prints saved file's name
        elif rerun in ['n', 'no']:
            print('Text file has not been saved.')
        else:
            print('ERROR: function "' + (selectAction) + '" is not a valid function. Please run and try again!')
            imgAction()
    imgAction()