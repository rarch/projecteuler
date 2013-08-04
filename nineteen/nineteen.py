#!/usr/bin/env python

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

daysInMonth={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
daysInWeek=7

def main():
    first_sundays=0
    days_off=6 # started on a monday
    for year in xrange(1900,2000+1):
        for month in xrange(1,12+1):
            if (days_off == 0) and (year>1900):
                first_sundays = first_sundays+1

            days_off = (days_off + daysInMonth[month])

            if (month == 2) and ( (not(year%4) and (year%100)) or (not(year%400)) ):
                days_off = days_off + 1 # it is february, on a fourth year or a fourth centry

            days_off=days_off% daysInWeek
    print first_sundays

if __name__ == "__main__":
    main()