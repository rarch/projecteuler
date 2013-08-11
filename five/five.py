#!/usr/bin/env python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# import os, sys
# dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
# util_dir = dirname+"/../util/"
# sys.path.append(util_dir)

# from util import factor
# from operator import mul

def unfactor(mylist):
    return reduce(mul,[a**b for (a,b) in mylist])

def unfactor_alt(mylist):
    product=1
    for (n,times) in mylist:
        product=product*(n**times)
    return product

def lcm_alt(listofints):
    factors=dict()
    for d in map(dict,map(factor, listofints)):
        for key in d.keys():
            if (not factors.has_key(key)) or (d[key]>factors[key]):
                factors[key]=d[key]
    return(unfactor(factors.items()))

def main_alt():
    print lcm_alt([i for i in xrange(1,21)])

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b / gcd(a,b) # // gcd(a,b)

def main():
    print reduce(lcm,[i for i in xrange(1,21)],1)

if __name__ == "__main__":
    main()