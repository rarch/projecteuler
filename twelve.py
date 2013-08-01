#!/usr/bin/env python

def getTri(n):
    tri=0
    if n>0:
        while n>0:
            tri=tri+n
            n=n-1
    return tri

first = lambda e: e[0]
primefactors = lambda factorization: map(first,factorization)

# print primefactors(factor(getTri(1000)))

def factors(n):
    return set(reduce(list.__add__,([i,n/i] for i in range(1,int(n**0.5)+1)if n%i==0)))

i=fs=0
while (fs<=500):
    i=i+1
    tri = getTri(i)
    fs = len(factors(tri))

print tri