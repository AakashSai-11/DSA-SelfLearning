'''
Q. The given question is that the list of queries will be given and we have to give the smallest prime factors of each of the 
query. For example, q = [10, 20, 60] then the answer should be similar to this -> [[2,5], [2,2,5], [2,2,3,5]]. Basically the
smallest prime factors possible for a number.

APPROACH 1 -> One of the ways to do this making use of prime_factors_of_a_number method which has already been taught, the code 
is something like this :

    def primeFactorisation(n):
        i = 2
        while i <= sqrt(n):
          if n%i==0:
            while n%i==0:
              n = n/i
              list.append(i)
          i+=1
        if n!= 1:
        list.append(n)
    
    for i in q:
      li = primeFactorisation(i)
      print(li)
    
    -> This works but the TC will be O(Q * sqrt(N)). This can be optimised!
    
APPROACH 2 -> As we have learnt, we will be using a slight variation of sieve of eratosthenes for more efficiency :

    answer = []
    spf = []
    for i in range(10**5+1):
      spf.append(i)
    
    spf[0],spf[1] = -1,-1
    i = 2
    while(i*i <= n):
      if spf[i] == i:
        for j in range(i*i, 10**5 + 1,i ):
          if spf[j] == j:
            spf[j] = i
    
    for k in q:
      li = []
      while k != 1:
        li.append(spf[k])
        k /= spf[k]
        
    -> The time complexity of this is O(q * log₂(n)) + O(n * loglog(n)) which is better than the first one!

'''