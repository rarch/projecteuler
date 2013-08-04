#!/usr/bin/env python

# n! means n * (n - 1) * ... * 3 * 2 * 1
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

from util import sumDig
from math import factorial

def remove_end_zeros(i):
    if (i and (i%10)) or not i:
        return i
    return remove_end_zeros(i/10)

# take advantage of python with large numbers
def main():
    print sumDig(factorial(100))

def main_alt():
    f=1
    for i in xrange(100):
        f=remove_end_zeros(f*(i+1))
    print sumDig(f)

if __name__ == "__main__":
    main()
