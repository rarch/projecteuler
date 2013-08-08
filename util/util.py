# utilities used for solving multiple problems

numbers={0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",\
    11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",\
    18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",\
    80:"eighty",90:"ninety",100:"hundred",1000:"thousand",1000000:"million",1000000000:"billion",\
    1000000000000:"trillion",1000000000000000:"quadrillion",1000000000000000000:"sextillion",\
    1000000000000000000000:"septillion",1000000000000000000000000:"octillion"}

thouPowers={0:"",1:"thousand",2:"million",3:"billion",4:"trillion",5:"quadrillion",6:"quintillion",7:"sextillion",\
    8:"septillion",9:"octillion"}

def factor(mN):
    i,times,factors=2,0,[]
    while mN>1:
        if all([i%f for (f,x) in factors]) and not (mN%i):
            # print i
            while not(mN%i):
                mN=mN/i
                times=times+1
            factors=factors+[(i,times)]
        i,times=i+1,0
    return factors

def fread(fn):
    with open(fn,'r') as f:
        data=f.read()
    return data

def freadlines(fn):
    with open(fn,'r') as f:
        lines=f.readlines()
    return lines

def generate_factors(n):
    if (n==1):
        return []
    for factor in xrange(2,n+1):
        if (n%factor==0):
            break
    return [factor] + generate_factors(n / factor) 

def nonZeroToWord(n,delim=None):
    if n<0:
        return " ".join(['negative',nonZeroToWord(-n,delim)])
    if n<1000:
        return upto999(n,delim)

    l=len(str(n))
    divisor,i=1000,1
    while (n/divisor)>1000:
        divisor=divisor*1000
        i=i+1

    return " ".join([upto999((n/divisor),delim),\
                     thouPowers[i],\
                     nonZeroToWord(n-divisor*(n/divisor),delim)])

def numToWord(n,delim=None):
    return nonZeroToWord(n,delim) if n else "zero"

def sumDig(n):
    digits = map(int,str(n))
    return sum(digits)

# returns max sum of a path down a triangle of ints shaped like pascal's traingle
def triangle(rows):
    for r,i in [(r,i) for r in xrange(len(rows)-2,-1,-1) for i in xrange(0,r+1)]:
        rows[r][i] = rows[r][i] + max([rows[r+1][i],rows[r+1][i+1]])

    return rows[0][0]

def upto99(n):
    if n in numbers.keys():
        return numbers[n]
    return "-".join([numbers[(n/10)*10],numbers[n%10]])

def upto999(n,delim=None):
    if n<100:
        return upto99(n)
    if not n%100:
        return " ".join([numbers[n/100],numbers[100]])
    return " ".join([numbers[n/100],numbers[100], delim ,upto99(n%100)]) if delim else \
        " ".join([numbers[n/100],numbers[100],upto99(n%100)])
