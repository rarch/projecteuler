#!/usr/bin/env ruby

UTIL="util"
UTIL_DIR="../#{UTIL}"

require File.join(File.dirname(__FILE__), "#{UTIL_DIR}", "#{UTIL}")
include Util

def main
    exit 1 if ARGV.length!=1

    i=ARGV[0].to_i
    
    exit 2 if i==0
    exit 3 if i<0

    puts Util::nonZeroToWord(i,nil).gsub(' ','').gsub('-','')
end

if __FILE__==$0
    main()
end