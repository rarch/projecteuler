--The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
--Find the sum of all the primes below two million.

import Util

ten = sum (takeWhile (<2000000) primes)

main = do
    let result = ten
    print result