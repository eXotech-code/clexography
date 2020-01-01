#!/usr/bin/env python3

import argparse
import clexEnc
import clexDec

version = '2.0'
name = 'clexography'
usage = name+' '+' '+version

#command line arguments
parser = argparse.ArgumentParser(prog=name, usage=usage)
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
    clexEnc.clexEnc(readFile, writeFile)
elif args.decode:
    readFile = args.decode[0]
    writeFile = args.decode[1]
    clexDec.clexDec(readFile, writeFile)