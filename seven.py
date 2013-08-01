#!/usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def brutesieve(index):
    p,primes=2,[]
    while len(primes)<index:
        if all([(p%f) for f in primes]):
            primes=primes+[p]
            # print p
        p=p+1
    return primes

# much faster, does not check unnecessary high prime factors
def quicksieve(index):
    cand,primes=3,[2]
    while len(primes)<index:
        if not primes:
            primes=[cand]
        for p in primes:
            if ((p**2)>cand):
                primes=primes+[cand]
                break
            if 0==(cand%p):
                break
        cand=cand+1

    return primes

# primes=quicksieve(6)
primes=quicksieve(10001)
print primes[-1]
