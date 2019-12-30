#!/usr/bin/env python3

import argparse
import clexEnc
import clexDec
import clexStr

parser = argparse.ArgumentParser(prog=clexStr.name, usage=clexStr.usage)
parser.add_argument("-v", "--version", help="show %(prog)s version", action="store_true")
actionGroup = parser.add_mutually_exclusive_group()
actionGroup.add_argument("-e", "--encode", help="encode image", nargs=2)
actionGroup.add_argument("-d", "--decode", help="decode image", nargs=2)

args = parser.parse_args()

if args.version:
    print(clexStr.version)
elif args.encode:
    readFile = args.encode[0]
    writeFile = args.encode[1]
    clexEnc.encode()
elif args.decode:
    clexDec.decode()