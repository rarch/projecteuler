# utilities used for solving multiple problems
module Util
    # generate all factors of a number
    def generate_factors(n)
        return [] if n == 1
        factor = (2..n).find {|x| n % x == 0} 
        [factor] + generate_factors(n / factor) 
    end

    # sieve of eratosthenes up to n
    def better_sieve_upto(n)
        s = (0..n).to_a
        s[0] = s[1] = nil
        s.each do |p|
            next unless p
            break if p * p > n
            (p*p).step(n, p) { |m| s[m] = nil }
        end
        s.compact
    end

end