#!/usr/bin/env ruby

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main
    multiple = 1
    (1..20).each do |val|
        multiple = multiple.lcm val
    end
    puts "#{multiple}"
end

if __FILE__==$0
    main()
end