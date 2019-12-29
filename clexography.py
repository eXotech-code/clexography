# imports
import imgconv
import txtconv

def main():
    # select img >> txt or txt >> img
    print('Welcome to Clexography!')
    selectAction = input('Do you want to encode (image >> text) or decode (text >> image)? (e/d): ')
    if (selectAction == 'e') or (selectAction == 'E') or (selectAction == 'encode') or (selectAction == 'Encode'):
        imgconv.imageText()
    elif (selectAction == 'd') or (selectAction == 'D') or (selectAction == 'decode') or (selectAction == 'Decode'):
        txtconv.textImage()
    else:
        print('ERROR: function "' + (selectAction) + '" is not a valid function. Please run and try again!')
        rerun = input('Do you want to rerun the program? (Y/n): ')
        if (rerun == 'y') or (rerun == 'Y') or (rerun == 'yes') or (rerun =='Yes'):
            main()
        else:
            print('Exiting...')


main()