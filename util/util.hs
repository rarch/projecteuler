--utilities used for solving multiple problems

module Util where

fibs :: [Integer]
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

fibs' :: [Integer]
fibs' = 1 : 1 : next fibs'
  where
    next (a : t@(b:_)) = (a+b) : next t

primeFactors :: Integer -> [Integer]
primeFactors n = factor n primes
  where
    factor n (p:ps) 
        | p*p > n        = [n]
        | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
        | otherwise      = factor n ps

primes :: [Integer]
primes = 2 : filter ((==1) . length . primeFactors) [3,5..]