#!/usr/bin/env ruby

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

MAX=999

def main
    mSum=0
    for n in 1..MAX
        if (0==n%3) or (0==n%5)
            mSum+=n
        end
    end

    puts mSum
end

if __FILE__==$0
    main()
end