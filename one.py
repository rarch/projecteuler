#!/usr/bin/env python

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# mSum=0
# for i in xrange (1,1001):
#     if (0==i%3 or 0==i%5):
#         mSum+=i

# print mSum

print sum([i for i in xrange(1,1000) if (0==i%3 or 0==i%5)])