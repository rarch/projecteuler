
--A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
--Find the largest palindrome made from the product of two 3-digit numbers.

four :: Integer
four = maximum [p | a<-[100..999], b<-[a..999], let p=a*b, let s=show p, s==reverse s] --need show to test string

main = do
    let result = four
    print result