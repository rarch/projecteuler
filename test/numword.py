#!/usr/bin/env python

import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
util_dir = dirname+"/../util/"
data_dir = dirname+"/../data/"
sys.path.append(util_dir)

from util import nonZeroToWord
import argparse

def main():
    parser = argparse.ArgumentParser(description='converts number to word')
    parser.add_argument('i', type=int, help='give a positive integer')
    args = parser.parse_args()

    i=args.i

    if (i==0):
        exit(1)
    if (i<0):
        exit(2)

    print nonZeroToWord(i).replace(" ","").replace("-","")

if __name__ == "__main__":
    main()