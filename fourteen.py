#!/usr/bin/env python

# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def nextCollatz(n):
    if n<1:
        raise ValueError('must pass positive integer')
    return 1 if n==1 else (3*n)+1 if n%2 else n/2

def CollatzLen(i):
    if i==1:
        return 1
    return 1+CollatzLen(nextCollatz(i))

LIM=1000000

def main():
    max_l=0
    for i in xrange(1,LIM):
        l=CollatzLen(i)
        if l>max_l:
            max_l=l
            max_i=i
    print max_i

# val -> under => nxt,1
# val -> over * i -> under => nxt(i*).nxt,1+i
# 1 -> 1 => 1,0
def nextColUnderLimAndDist(i,lim=1000000):
    if i==1:
        return 1,0 # multiple returns
    thenext,dist=nextCollatz(i),1
    while thenext>=lim:
        thenext,dist=nextCollatz(thenext),dist+1
    return thenext,dist # multiple returns

def main_alt():
    from collections import deque

    notAddedItem_Queue=deque([i for i in xrange(2,LIM)]) # popleft
    Dictionary={ 1:1 } # d[w]=val
    toAddItem_Stack=deque() # append, pop

    max_v=0

    while notAddedItem_Queue:

        first = notAddedItem_Queue.popleft()
        second,d_first_second=nextColUnderLimAndDist(first,LIM)

        toAddItem_Stack.append((first,second,d_first_second))

        while toAddItem_Stack:
            _,next,_ = toAddItem_Stack[-1]
            if next in Dictionary:
                a,b,d_ab=toAddItem_Stack.pop()
                v=Dictionary[b]+d_ab
                Dictionary[a]=v
                if v>max_v:
                    max_v=v
                    max_i=a
            else:
                notAddedItem_Queue.remove(next)
                nextnext,d_nextnext = nextColUnderLimAndDist(next,LIM)
                toAddItem_Stack.append((next,nextnext,d_nextnext))

    print max_i
    # print max(Dictionary.items(), key=lambda (num,val):val)[0]

if __name__ == "__main__":
    main()
