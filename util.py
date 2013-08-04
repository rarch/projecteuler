#!/usr/bin/env python

# utilities used for solving multiple problems

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

def fread(fn):
    with open(fn,'r') as f:
        data=f.read()
    return data

def freadlines(fn):
    with open(fn,'r') as f:
        lines=f.readlines()
    return lines

# returns max sum of a path down a triangle of ints shaped like pascal's traingle
def triangle(rows):
    for r,i in [(r,i) for r in xrange(len(rows)-2,-1,-1) for i in xrange(0,r+1)]:
        rows[r][i] = rows[r][i] + max([rows[r+1][i],rows[r+1][i+1]])

    return rows[0][0]