#!/usr/bin/env python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# faster sieve, similar to the one in seven
def quicksieve(lim):
    cand,primes=3,[2]
    while cand<lim:
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

def main():
    primes=quicksieve(2000000)
    print sum(primes)

if __name__ == "__main__":
    main()