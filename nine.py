#!/usr/bin/env python
ispythagorean=lambda a,b,c:a**2 + b**2 == c**2

for a in xrange(1,1000):
    for b in xrange(a,1000):
        c=1000-a-b
        if ispythagorean(a,b,c):
            print a*b*c #a,b,c,