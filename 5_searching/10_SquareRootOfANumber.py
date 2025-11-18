'''
Using linear search will have the TC of O(sqrt(n)) and this binary search will have the TC of P(logn)
'''

def squareRoot(num):
    low = 0
    high = num
    ans = 1
    while low <= high:
        mid = low + (high-low)//2
        
        if mid**2 <= num:
            ans = mid
            low = mid+1
        else:
            high = mid-1
    
    return ans

print(squareRoot(28))