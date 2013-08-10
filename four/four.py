#!/usr/bin/env python

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import product

# palindromic=lambda val: val==int(''.join(reversed([c for c in str(val)])))
# palindromic=lambda num: str(num) == str(num)[::-1]

def palindromic_alt(val):
    return (val==int(''.join(reversed([c for c in str(val)]))))

def palindromic(num):
    return (str(num)==str(num)[::-1])

def main_alt():
    multiples = ( (a, b) for a, b in product(xrange(100,1000), repeat=2) if palindromic_alt(a*b) )
    print (lambda e:(e[0],e[1],e[0]*e[1])) (max(multiples, key=lambda (a,b): a*b))[-1]

def main():
    # palindromic = lambda n: str(n)==str(n)[::-1]
    print max( a*b for a, b in product(xrange(100,1000), repeat=2) if str(a*b)==str(a*b)[::-1] ) #palindromic(a*b))

if __name__ == "__main__":
    main()