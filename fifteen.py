#!/usr/bin/env python

# Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20*20 grid?

l,w=20,20

def factorial(n):
    if n<0:
        raise ValueError('must pass positive integer')
    if n==0:
        return 1
    return n*factorial(n-1)

def choose(n,k):
    return factorial(n)/factorial(k)/factorial(n-k)

print choose(l+w,l)

# path=''
# for i in xrange(0,l):
#     path=path+'d'
# for i in xrange(0,w):
#     path=path+'r'

# # paths=set([''.join(p) for p in [i for i in permutations(path,len(path))]])
# paths=set([i for i in permutations(path,len(path))])
# numpaths=len(paths)
# print numpaths