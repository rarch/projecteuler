#!/usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def sieve(index):
    p,primes=2,[]
    while len(primes)<index:
        if all([(p%f) for f in primes]):
            primes=primes+[p]
            # print p
        p=p+1
    return primes

# def sieve(index):
#     p,primes=2,[]
#     while len(primes)<index:
#         for f in primes:
#             if not(p%f):
#                 break
#             if f**2 > p:
#                 primes=primes+[p]
#                 break
#         p=p+1

#     return primes

# primes=sieve(6)
primes=sieve(10001)
print primes[-1]
