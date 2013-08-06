--utilities used for solving multiple problems
module Util where

fibs = 1 : 1 : zipWith (+) fibs (tail fibs)

fibs' = 1 : 1 : next fibs'
  where
    next (a : t@(b:_)) = (a+b) : next t