#!/usr/bin/env python

# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def ispythagorean(a,b,c):
    return (a**2 + b**2 == c**2)

def main():
    for a in xrange(1,1000):
        for b in xrange(a,1000):
            c=1000-a-b
            if ispythagorean(a,b,c):
                print a*b*c #a,b,c,

if __name__ == "__main__":
    main()