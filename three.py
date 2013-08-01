#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def factor(mN):
    i,times,factors=2,0,[]
    while mN>1:
        if all([i%f for (f,x) in factors]) and not (mN%i):
            # print i
            while not(mN%i):
                mN=mN/i
                times=times+1
            factors=factors+[(i,times)]
        i,times=i+1,0
    return factors

if __name__ == "__main__":
    mN=600851475143
    print [f for (f,x) in (factor(mN))][-1]