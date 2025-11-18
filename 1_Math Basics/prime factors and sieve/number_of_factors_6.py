'''
Q. we are given n where we have to give the array from 1 to n and the value of that array should be number of factors of all the 
respective numbers, for example if 6 is given the answer should be [1,2,2,3,2,4], The number of factors of 1 is 1, 2 is 2, 3 is 3, 4 is 4, 5 is 1
and 6 is 4
'''

def number_of_factors(n):
    factors = [1 for i in range(n+1)]
    i = 2
    while i <= n:
        for j in range(i,n+1,i):
            factors[j] += 1
        i += 1
    
    print(factors)

number_of_factors(6)


