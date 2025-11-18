'''

The gcd of two numbers refers to greatest common divisor of the two numbers, for example the gcd of 4,6 is 2 as factors of 4
are 1,2,4 and for 6 it is 1,2,3,6. The greatest common divisor between them is obviously 2.

APPROACH 1 -> The most naive approach is to iterate from 1 to the smallest of two numbers and the factor that divides both the 
numbers will be assigned to a temporary variable, The TC is O(min(a,b)) where a,b are two given numbers

  a = int(input())
  b = int(input())
  gcd = 0
  for i in range(1, min(a,b)+1):
    if a%i == 0 and b%i==0:
      gcd = i
  print(gcd)
  
  -> This can be improved!
  
APPROACH 2 -> This is based on the eucleadean algorithm, where the process goes like this:
                        4)6(1
                          4
                         ----
                          2)4(2
                            4
                           ----
                            0 -> We repeat this division and whenever we get 0 we stop it and return the latest divisor which is 
                                 2 in this case so the gcd of 4 and 6 is 2
                                 
            def gcd(a,b):
                if b==0:
                    return a
                if a<b:
                    a,b = b,a
                
                return gcd(b, a%b)
                
            -> This is O(log(n)) TC and much better than the previous one
    
### Some points for gcd:

1. If you divide the two numbers with gcd then you get relative primes which means that the common factor between two of them is 1
and it is the same to get simplest fraction of two numbers, we divide them with the gcd.

2. Cost of gcd is asked in some problems where we add a//b during the process, its more like how many times b is subtracted in a
or something like that. 

3. For a number taking an example of 38, if we keep on doing the sum of digits until the sum reaches a single digit:-
38 -> 3+8 -> 11 -> 1+1 -> 2 => We are done here as the sum converges to single digit. To get the final sum we have a formula and 
that is ===== (1 + (num - 1)) % 9 ===== . This works for every number except 0


'''