#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import os, sys
dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
util_dir = dirname+"/../util/"
sys.path.append(util_dir)

from util import factor

def main():
    mN=600851475143
    print [f for (f,x) in (factor(mN))][-1]

if __name__ == "__main__":
    main()