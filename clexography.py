#!/usr/bin/env python3

# imports
import imgconv
import txtconv

def main():
    # select img >> txt or txt >> img
    print('Welcome to Clexography!')
    selectAction = input('Do you want to encode (image >> text) or decode (text >> image)? (e/d): ').lower()
    if selectAction in ['e', 'encode']:
        imgconv.imageText()
    elif selectAction in ['d', 'decode']:
        txtconv.textImage()
    elif (selectAction == 'exit'):
        print('Exiting...')
    else:
        rerun = input('ERROR: function"' + selectAction + '"is not a valid function. Do you want to run again? (Y/n): ').lower()
        if rerun in ['y', 'yes']:
            main()
        else:
            print('Exiting...')

main()