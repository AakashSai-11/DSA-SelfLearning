'''
Q. We are given list of queries where len(queries) <= 10*5, the queries consist of lists of L,R i.e,
for example, queries = [[3,10], [8,20], [1,5]]. Now for every L,R pair; We need to find out the number of primes which mean the
answer for the example one will be [3, 4, 3].
Constraints = 1 <= L <= R <= 10*6


APPROACH 1 -> The extreme naive solution or brute force approach will be :

    answer = []
    for i in range(len(queries)):
      count = 0
      for j in range(i[0], i[1]):
        if isPrime(j):
          count += 1
      answer.append(count)
    print(answer)
    
    The time complexity is O(Q * (r-l+1) * sqrt(n)), because the outer loop runs for len(queries) times, second loop always runs from
    l to r and the isPrime function takes sqrt(N). This is massive and well, though easy not at all recommended!
    

APPROACH 2 -> Looking at the previous solution, we can look at the perspective where we can try to optimise the sqrt(N) part and 
try to make the isPrime part O(1) operation. Now that we know about sieve algorithm, we make use of it and remove that isPrime part.

    function getSieve(n):
      arr = [1] * (n+1)
      arr[0], arr[1] = 0,0
      for i in range(2,n**0.5+1):
        if arr[i] == 1:
          for j in range(2*i, n+1, i):
            arr[j] = 0
      return arr
    
    -> As we previously saw, This will give us the sieve/array where we get all the prime number upto number n, making use of this
    we continue with the second part of our code
    -> We know that the maximum possible number is R which is 10*6, so we make a sieve array for that thereby giving all the primes.
    
    prime = getSieve(10*6)
    answer = []
    for i in range(len(queries)):
      count = 0
      for j in range(i[0], i[1]):
        if prime[j] == 1:
          count += 1
      answer.append(count)
    print(answer)    
    
    -> For this method, we have removed that sqrt(n) part, well getting the sieve will take O(N log(logn)) time but it is nothing
    when compared to O(Q * (r-l+1)), so the overall TC still is O(Q * (r-l+1)). Well it can be seen as better solution definitely
    but is that it. We can still do better, Looking at this solution, if we think about optimising the second loop where we iterate
    through the L and R, the solution can be drastically improved because going through L and R once is fine but if we take the first
    example of [[3,10], [8,20], [1,5]]. We already calculate 3 to 10 for the first pair but then again we do some part in different
    pairs repeatedly. 1 to 5 is already calculated in the first pair so the idea of iterating through L and R for each case is 
    obviously not the way to go, We should think of some pre computation that will let us avoid this redundant process.
    This is the core idea for more improvement of the second approach or this approach. And this leads to our third approach.
    
APPROACH 3 -> If we think properly and deeply, well even if you do that you won't get it so just continue reading. To somehow 
remove that (r-l+1) TC, we use prefix sum method. What we do is we take that sieve array that we get from getSieve function, 
Considering the scenario with example for [1,10], we get the array [0,0,1,1,0,1,0,1,0,0,0] from the getSieve(10). The 1's indicate
prime numbers. Now if you use prefix sum method to calculate number of 1's appeared till that index and represent it in another
array, we can improve TC greatly. What I meant was using the above array to get [0,0,1,2,2,3,3,4,4,4,4], This indicates the no. of
prime numbers up till that index, I think now you got the idea of what I am saying about, If you really got this idea before reading
this shit then congratulations, atleast your future is not bleak. I think so.

Just in case if you dont know how to get that count array, its simple, you just have to take a count and keep iterating through
sieve array, you keep adding that to the count and replace the array index value with that count for every step. If you really
didn't know this before then you better think of some different field.
    
    
    arr = getSieve(10*6)
    count = 0
    prime = []*(10*6 + 1)
    for i in range(len(prime)):
      count += prime[i]
      prime[i] = count
      
    answer = []
    for i in range(len(queries)):
      no_of_primes = prime[i[1]] - prime[i[0]-1]
      answer.append(no_of_primes)
    print(answer)    
    
    -> The time complexity has now become O(N log(logN)) + O(10*6) + O(Q), This is extremely optimised and much better than the previous
    ones.
      
    
'''