#!/usr/bin/env python3

import argparse

version = '2.0'
name = 'Clexography'
usage = name+' '+' '+version

parser = argparse.ArgumentParser(prog=name, usage=usage)
parser.add_argument("-v", "--version", help="show %(prog)s version", action="store_true")
actionGroup = parser.add_mutually_exclusive_group()
actionGroup.add_argument("-e", "--encode", help="encode image", nargs=2)
actionGroup.add_argument("-d", "--decode", help="decode image", nargs=2)

args = parser.parse_args()

if args.version:
    print(version)
elif args.encode:
    readFile = args.encode[0]
    writeFile = args.encode[1]
    print(readFile)
    print(writeFile)
elif args.decode:
    print('decoding')