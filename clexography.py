#!/usr/bin/env python3

import sys
import argparse
import base64
import functions as fn

version = '2.0'
name = 'clexography'
usage = name+' '+' '+version

# if user specifies incorrect argument, program prints help screen
class argParser(argparse.ArgumentParser):
    def parseError(self, message):
        sys.stderr.write('ERROR: %s\n' % message)
        self.print_help()
        sys.exit

# command line arguments
parser = argParser()
parser.add_argument('-v', '--version', help='show %(prog)s version', action='store_true')
parser.add_argument('--nocheck', help='omit extension checker', action='store_false')       # --nocheck is an argument to omit extension checking
actionGroup = parser.add_mutually_exclusive_group()
actionGroup.add_argument('-e', '--encode', help='encode image', nargs=2)                    # encode argument takes 2 actions (for readFile and writeFile)
actionGroup.add_argument('-d', '--decode', help='decode image', nargs=2)                    # decode argument takes 2 actions (for readFile and writeFile)

args = parser.parse_args()

if args.version:
    print(version)
elif args.encode:
    readFile = args.encode[0]
    writeFile = args.encode[1]
    # writeFile path first runs through extension checker
    if args.nocheck:    # unless --nocheck is specified
        fn.extCheck(sys, writeFile)
    fn.txtEncode(base64, readFile, writeFile)
elif args.decode:
    readFile = args.decode[0]
    writeFile = args.decode[1]
    # writeFile path first runs through extension checker
    if args.nocheck:    # unless --nocheck is specified
        fn.extCheck(sys, writeFile)
    fn.txtDecode(base64, readFile, writeFile)

# if no arguments are specified, program prints help screen
if len(sys.argv)==1:
    print('No arguments specified. Printing help screen...\n')
    parser.print_help(sys.stderr)
    sys.exit()