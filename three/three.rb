#!/usr/bin/env ruby

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

require File.join(File.dirname(__FILE__), '../util', 'util')
include Util

N = 600851475143

def main
    largest=Util::generate_factors(N)[-1]
    puts "#{largest}"
end

if __FILE__==$0
    main()
end