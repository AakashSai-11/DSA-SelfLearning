'''
Q. Print all the prime factors of a number?
APPROACH 1 -> The extreme naive approach to solve this problem is to go from 2 to that number and checking every number which is divisible the 
given number and then checking whether it is prime or not

    while(i<=n):
      if n%i==0:
        if prime(i):
          list.add(i)
      i+=1
    
    -> As you can see the time complexity here is O(N*sqrt(N)) where the outer loop runs n times and the inner one had the sqrt(n) TC
    to check whether the number is prime or not
    
    => WE CAN OPTIMISE THIS AND WRITE SOME BETTER CODE!
    
APPROACH 2 -> The optimisation of the above can be done by cut shorting the outer loop which goes for n times, instead of doing that
we can simply go only for sqrt(n) iterations and take two divisors at once. So the code now becomes

    while(i<=sqrt(n)):
      if n%i==0:
        if prime(i):
          list.append(i)
        if n/i != i:
          if prime(n/i):
            list.append(n/i)
      i+=1
    
    -> The time complexity now becomes O(sqrt(N) * 2 * sqrt(N)) which is better than the previous one
    => WE CAN EVEN OPTIMISE THIS AND WRITE BETTER!
    
APPROACH 3 -> We follow prime factorisation method that is generally used in school to find out the prime factors, for example
if we take 780 as example first we divide by 2, to get 390 and again by 2 to get 195, we will see if it works again for 2. It doesn't so
now we move onto 3, we divide 195 by 3 to get 65 and now 3 and 4 both are not divisible now we move to 5, 65 by 5 and we get 13 and now
from 5 we move to every next number but we will finally end up with 13 as only 13 is divisible by 13. Thereby we get all the factors and that to
only prime factors which are => 2,3,5,13

    i = 2
    while i<=n:
      if n%i==0:
        list.append(i)
        while n%i==0:
          n = n/i
      i+=1
    
    -> If we consider this approach, the time complexity for 780 is O(13) as it runs 13 times, you may think it is optimised but if we
    consider large prime numbers like 37, this loop runs from 2 to 37 making it inefficient for larger prime numbers i.e, O(N) itself
    => EVEN THIS CAN BE OPTIMISED!
    
APPROACH 4 -> What if we just loop from 2 to sqrt(n) in this case, it works! It is fascinating but do the dry run for 780 and 37 for the below code

    i = 2
    while i <= sqrt(n):
      if n%i==0:
        list.append(i)
        while n%i==0:
          n = n/i
      i+=1
    if n!= 1:
      list.append(n)
      
    -> This is the most efficient way to do things as, it only takes 6 steps for a number like 780 and the TC is O(sqrt(N)*log(N))


'''