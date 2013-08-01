#!/usr/bin/env python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from three import factor

def unfactor(mylist):
    product=1
    for (n,times) in mylist:
        product=product*(n**times)
    return product

def lcm(listofints):
    factors=dict()
    for d in map(dict,map(factor, listofints)):
        for key in d.keys():
            if (not factors.has_key(key)) or (d[key]>factors[key]):
                factors[key]=d[key]
    # print factors.items()
    return(unfactor(factors.items()))

if __name__ == "__main__":
    # print lcm([i for i in xrange(1,10)])
    print lcm([i for i in xrange(1,21)])