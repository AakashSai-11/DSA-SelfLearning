'''
#Sieve of eratosthenes :

It is one of the famous algorithms in DSA,so the question we will be using it in is :

Q. Given a number n, print all the prime numbers till n?
-> If n is 10, we have to print 2,3,5,7 which are the prime numbers till 10

APPROACH 1 -> This is the extreme naive solution or bruteforce, where you iterate till n and you call isPrime function for every i.

    for i in range(2,n):
      if isPrime(i):
        print(i)
    
    -> The TC here is O(n * sqrt(n)) where the outer loop runs for all i and isprime function everytime runs for sqrt(n) times, it is a
    very expensive operation when the input is large, so not at all advisable.
    
APPROACH 2 -> I will take an array which will have some pre computation that will give me whether the number is a prime or not
in O(1) operation. Look at the code below:

    prime = [1]*n+1
    prime[0], prime[1] = 0,0
    for i in range(2,n+1):
      if prime[i] == 1:
        for j in range(2*i,n+1,i):
          prime[j] = 0
    
    for i in range(n):
      if prime[i] == 1:
        print(i)
        

The time complexity is a bit complex to explain but this can be optimized as well.

APPROACH 3 -> This is the optimized version of approach 2 and is mainly known as the sieve of eratosthenes, the code is written on main font.


'''

n = int(input())
prime = [1]* (n+1)
prime[0], prime[1] = 0,0
for i in range(2, int(n**0.5)+1):
    if prime[i] == 1:
        for j in range(i*i, n+1, i):
            prime[j] = 0

for i in range(n+1):
    if prime[i] == 1:
        print(i)
        
        
def seive(n):
  primes = [i for i in range(n + 1)]
  for i in range(2, int(n ** (0.5)) + 1):
    if primes[i] == i:
      for j in range(i * i, n + 1, i):
        primes[j] = i
  return primes

print(seive(20))

def prime_factorization(n):
  pf = {}
  i = 2
  while i * i <= n:
    while n % i == 0:
      n = n // i
      pf[i] = pf.get(i, 0) + 1
    i += 1
  return pf

print(prime_factorization(36))
    
        
'''
There are optimisations, where we dont need to start from every multiple like 2x2,2x3,2x4, its ok for 2 but when we think of 3, we
dont need to consider 3x2 and for 4 we dont need to consider 4x2, 4x3 and we can directly start from 4x4 so the second loop starts
from i*i and because the start is i*i, the upper loop dont need to cross sqrt(n) as crossing it will be a waste because it will
however not go into the second loop so the limit in the first one is set to the sqrt(n)

The time complexity for this algorithm is O(N) + O(Nlog(logN)) + O(N)
This is mathematically proven so no one will ask to derive this and we cant do that even if they ask us!
The SC is O(N)

'''

            