#!/usr/bin/env python3

import sys
import argparse
import encode
import decode

version = '2.0'
name = 'clexography'
usage = name+' '+' '+version

#command line arguments

class argParser(argparse.ArgumentParser):
    def parseError(self, message):
        sys.stderr.write('ERROR: %s\n' % message)
        self.print_help()
        sys.exit

parser = argParser()
parser.add_argument("-v", "--version", help="show %(prog)s version", action="store_true")
actionGroup = parser.add_mutually_exclusive_group()
actionGroup.add_argument("-e", "--encode", help="encode image", nargs=2)    #encode argument takes 2 actions (read write)
actionGroup.add_argument("-d", "--decode", help="decode image", nargs=2)    #decode argument takes 2 actions (read write)

args = parser.parse_args()

if args.version:
    print(version)
elif args.encode:
    readFile = args.encode[0]
    writeFile = args.encode[1]
    encode.txtEncode(readFile, writeFile)
elif args.decode:
    readFile = args.decode[0]
    writeFile = args.decode[1]
    decode.txtDecode(readFile, writeFile)
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit()