#!/usr/bin/env python

# Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20*20 grid?

def factorial(n):
    if n<0:
        raise ValueError('must pass positive integer')
    if n==0:
        return 1
    return n*factorial(n-1)

def choose(n,k): # use math
    return factorial(n)/factorial(k)/factorial(n-k)

def main():
    l,w=20,20
    print choose(l+w,l)

def main_alt():
    from itertools import permutations
    l,w=20,20
    path=''
    for i in xrange(0,l):
        path=path+'d'
    for i in xrange(0,w):
        path=path+'r'

    # paths=set([''.join(p) for p in [i for i in permutations(path,len(path))]])
    paths=set([i for i in permutations(path,len(path))])
    numpaths=len(paths)
    print numpaths

if __name__ == "__main__":
    main()