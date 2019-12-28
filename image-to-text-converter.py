# imports
import base64

# user specifies the file path
filePath = input('Input path of the image file: ')

# converter
with open(filePath, "rb") as imageFile:
    imagestr = base64.b64encode(imageFile.read())   # decodes image raw data into string
    print(imagestr)                                 # prints the text from image data

# saving as text file
confirm = input('Do you want to save this text as .txt file? (Y/n): ')
if confirm == "Y":
    savePath = input('Input path of the new text file (recomended .txt): ')
    text_file = open(savePath, "wb")                            # opens the specified file path for editing
    n = text_file.write(imagestr)                               # inserts image string to the text file
    text_file.close()
    print('Text file has been saved in: ' + (savePath))          # prints saved file's path
else:
    print('Text file has not been saved.')