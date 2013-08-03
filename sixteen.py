#!/usr/bin/env python

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def sumDig(n):
    digits = map(int,str(n))
    return sum(digits)

# def doubleIt(mstr):
#     l=len(mstr)
#     res=''
#     hi=0

#     for i in xrange(l-1,-1,-1):
#         dig = int(mstr[i])
#         ret = 2*dig + hi
#         hi = ret/10
#         res = str(ret%10)+res
#     if hi:
#         res = str(hi)+res
#     return res

# inpt='1'
# c=0
# while c<1000: 
#     inpt=doubleIt(inpt)
#     c=c+1

# s=0
# for i in xrange(0,len(inpt)):
#     s=s+int(inpt[i])
# print s

print sumDig(2**1000)