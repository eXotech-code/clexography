# imports
import base64

# select img >> txt or txt >> img
print('Welocome to Clexography!')
selectAction = input('Do you want to encode (image >> text) or decode (text >> image)? (encode/decode): ')
if selectAction == 'encode':
    # user specifies the file path
    filePath = input('Input path of the image file: ')

    # converter
    with open(filePath, 'rb') as imageFile:
        imagestr = base64.b64encode(imageFile.read())   # decodes image raw data into string
        print(imagestr)                                 # prints the text from image data

    # saving as text file
    confirm = input('Do you want to save this text as .txt file? (Y/n): ')
    if confirm == 'Y' or 'y' or 'yes' or 'yep' or 'Yes' or "yeah mate, brin' it on":
        savePath = input('Input path of the new text file (recomended .txt): ')
        text_file = open(savePath, 'wb')                            # opens the specified file path for editing
        n = text_file.write(imagestr)                               # inserts image string to the text file
        text_file.close()
        print('Text file has been saved in: ' + (savePath))          # prints saved file's path
    elif confirm == 'n' or 'N' or 'no' or 'nope' or 'No':
        print('Text file has not been saved.')
    else:
        print('ERROR: function not determined correctly. Please run and try again!')
elif selectAction == 'decode':
    # user inputs text file path
    filePath = input('Input path of the text file: ')

    # program reads the text file
    with open(filePath, 'rb') as textFile:
        imagestrRaw = textFile.read()

    # converting bytes to utf-8
    imagestr = base64.b64decode(imagestrRaw)

    # user inputs folder to which the converted image file will be saved
    folderPath = input('Please input directory to save decoded-image.png in (enter "." to save to current working directory): ')

    # writing converted string to image file
    with open(folderPath + '/decoded-image.png', 'wb') as imageFile:        # path to the file is predetermined (will change in the future)
        imageFile.write(imagestr)
        imageFile.close()

    print('Operation completed successfully!')
    print('File saved in ' + folderPath + '/decoded-image.png')
else:
    print('ERROR: function not determined correctly. Please run and try again!')