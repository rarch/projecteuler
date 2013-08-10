#!/usr/bin/env ruby

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

UTIL="util"
UTIL_DIR="../#{UTIL}"

require File.join(File.dirname(__FILE__), "#{UTIL_DIR}", "#{UTIL}")
include Util

REALLY="and" # is that really necessary? only for decimals, right?
# REALLY=nil

def main
    s=0
    (1..1000).each do |n|
        s=s+(Util::numToWord(n,REALLY)).gsub(' ','').gsub('-','').length
    end
    puts "#{s}" # print s # puts s.to_s
end

if __FILE__==$0
    main()
end