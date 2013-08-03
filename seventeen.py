#!/usr/bin/env python

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

numbers={0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",\
    11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",\
    18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",\
    80:"eighty",90:"ninety",100:"hundred",1000:"thousand",1000000:"million",1000000000:"billion",\
    1000000000000:"trillion",1000000000000000:"quadrillion",1000000000000000000:"sextillion",\
    1000000000000000000000:"septillion",1000000000000000000000000:"octillion"}

thouPowers={0:"",1:"thousand",2:"million",3:"billion",4:"trillion",5:"quadrillion",6:"quintillion",7:"sextillion",\
    8:"septillion",9:"octillion"}

REALLY='and'

def upto99(n):
    if n in numbers.keys():
        return numbers[n]
    return ' '.join([numbers[(n/10)*10],numbers[n%10]])

def upto999(n):
    if n<100:
        return upto99(n)
    if not n%100:
        return ' '.join([numbers[n/100],numbers[100]])
    return ' '.join([numbers[n/100],numbers[100], REALLY ,upto99(n%100)]) 

def numToWord(n):
    if n<1000:
        return upto999(n)

    l=len(str(n))
    divisor,i=1000,1
    while (n/divisor)>1000:
        divisor=divisor*1000
        i=i+1

    return ' '.join([upto999((n/divisor)),\
                     thouPowers[i],\
                     numToWord(n-divisor*(n/divisor))])

s=0
for i in xrange(1,1001):
    # print numToWord(i)
    s=s+len(numToWord(i).replace(' ',''))

print s
