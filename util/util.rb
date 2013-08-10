# utilities used for solving multiple problems
module Util

    $numbers={0=>"",1=>"one",2=>"two",3=>"three",4=>"four",5=>"five",6=>"six",7=>"seven",8=>"eight",9=>"nine",10=>"ten",
        11=>"eleven",12=>"twelve",13=>"thirteen",14=>"fourteen",15=>"fifteen",16=>"sixteen",17=>"seventeen",
        18=>"eighteen",19=>"nineteen",20=>"twenty",30=>"thirty",40=>"forty",50=>"fifty",60=>"sixty",70=>"seventy",
        80=>"eighty",90=>"ninety",100=>"hundred",1000=>"thousand",1000000=>"million",1000000000=>"billion",
        1000000000000=>"trillion",1000000000000000=>"quadrillion",1000000000000000000=>"sextillion",
        1000000000000000000000=>"septillion",1000000000000000000000000=>"octillion"}

    $thouPowers={0=>"",1=>"thousand",2=>"million",3=>"billion",4=>"trillion",5=>"quadrillion",6=>"quintillion",7=>"sextillion",
        8=>"septillion",9=>"octillion"}

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

    def nonZeroToWord(n,delim)
        return [ 'negative', nonZeroToWord(-n,delim) ].join(" ") if n<0
        return upto999(n,delim) if n<1000

        l=n.to_s.length
        divisor=1000
        i=1
        while (n/divisor)>1000 do
            divisor=divisor*1000
            i+=1
        end

        [ upto999((n/divisor),delim), $thouPowers[i], nonZeroToWord(n-divisor*(n/divisor),delim) ].join(" ")
    end

    def numToWord(n,delim) # can pass nill
        return nonZeroToWord(n,delim) if n!=0
        "zero"
    end

    def upto99(n)
        return $numbers[n] if $numbers.has_key?(n)
        [ $numbers[(n/10)*10], $numbers[n%10] ].join("-")
    end

    def upto999(n,delim)
        return upto99(n) if n<100
        return [ $numbers[n/100], $numbers[100] ].join(" ") if (n%100)==0
        return [ $numbers[n/100], $numbers[100], delim, upto99(n%100) ].join(" ") if delim
        [ $numbers[n/100], $numbers[100], upto99(n%100) ].join(" ")
    end
end