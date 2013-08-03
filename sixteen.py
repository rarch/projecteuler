#!/usr/bin/env python

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def sumDig(n):
    digits = map(int,[d for d in str(n)])
    return sum(digits)

print sumDig(2**1000)