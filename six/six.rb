#!/usr/bin/env ruby

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def main
    sum, ssq = 0, 0
    100.downto(1) { |x| sum+=x; ssq += (x*x) }
    res = sum**2 - ssq
    puts "#{res}"
end

if __FILE__==$0
    main()
end