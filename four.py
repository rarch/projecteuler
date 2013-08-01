#!/usr/bin/env python

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import product

# palindromic=lambda val: val==int(''.join(reversed([c for c in str(val)])))
palindromic=lambda num: str(num) == str(num)[::-1]

# multiples = ( (a, b) for a, b in product(xrange(100,1000), repeat=2) if palindromic(a*b) )
# print (lambda e:(e[0],e[1],e[0]*e[1])) (max(multiples, key=lambda (a,b): a*b))

print max( a*b for a, b in product(xrange(100,1000), repeat=2) if palindromic(a*b) )