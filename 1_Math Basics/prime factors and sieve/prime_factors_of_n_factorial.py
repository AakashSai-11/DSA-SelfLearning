'''
Q. Given an integer n, for example 10, we have to find prime factors or basically count of all prime factors of that number
Ex -> 10 factorial :-
        That means 100 can be written as 10x9x8x7x6x5x4x3x2x1 and 2 happens to be 8 times
        count = {
            2 : 8,
            3 : 4,
            5 : 2,
            7 : 1
        }
        
APPROACH -> The code is given below :-

'''

def prime_factors_of_n_factorial(n):
    sieve = [1 for i in range(n+1)]
    i = 2
    while i*i <= n:
        if sieve[i] == 1:
            for j in range(i*i, n+1, i):
                sieve[j] = i
        i += 1
    
    
    count_dict = {}
    
    for i in range(2, n+1):
        count = 0
        p = 1
        if sieve[i] == 1:
            print(i, p)
            while n//(i**p) > 0:
                count += n//(i**p)
                p += 1
                print(i, p)
            count_dict[i] = count_dict.get(i, count)
        
    print(count_dict)

prime_factors_of_n_factorial(10)