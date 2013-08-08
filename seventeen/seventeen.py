#!/usr/bin/env python

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
util_dir = dirname+"/../util/"
data_dir = dirname+"/../data/"
sys.path.append(util_dir)

from util import numToWord

REALLY="and" # is that really necessary? only for decimals, right?

def main():
    s=0
    for i in xrange(1,1001):
        s=s+len(numToWord(i,REALLY).replace(" ","").replace("-",""))

    print s

if __name__ == "__main__":
    main()
