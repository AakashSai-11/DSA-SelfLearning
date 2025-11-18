'''
So this question is all about generalising the fibonacci series, For example:

Input :
k = 3, n = 6
start = [0, 1, 2]

Output :
[0, 1, 2, 3, 6, 11]

Explanation :

The sequence starts with [0, 1, 2], and each subsequent number is the sum of the previous k numbers:

-> 3 is the sum of 0 + 1 + 2
-> 6 is the sum of 1 + 2 + 3
-> 11 is the sum of 2 + 3 + 6

So this is the problem, Basically we have to write the code to generalise the fibonacci series for k number

'''

n = int(input())
k = int(input())
start = list(map(int, input().split()))
arr = start.copy()

def general(arr, n, k):
    if len(arr) == n:
        return arr
    temp = sumfunc(arr, -1, k)
    arr.append(temp)
    return general(arr, n, k)
    
def sumfunc(arr, check, k):
    if check == -k-1:
        return 0
    return arr[check] + sumfunc(arr, check-1, k)
    
print(general(arr, n, k))
            