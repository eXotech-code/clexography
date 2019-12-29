# imports
import base64

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