'''
This is the most efficient searching algorithm used across the globe when the array or list is sorted or that may be any datastructure
but for this algo to work, the data should be sorted 

Ofcourse this can be written in two ways:
1. Iterative way
2. Recursive way

The TC of binary search is O(logn) and SC is O(1)  --> Very very efficient

'''

def binarySearch(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <=  high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binarySearch([2,4,6,8,10,12], 1))
# This is the iterative way of doing it

def bin_search(arr, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return bin_search(arr, mid+1, high, target)
    else:
        return bin_search(arr, low, mid-1, target)
    
print(bin_search([2,4,6,8,10,12],0,5, 8))
# So beautiful, This is the recursive way of doing it

# The good practice of calculating mid is in this way :

# mid = low + ((high - low)//2)   --> You can expand this, It is equal to our ordinary way of doing it, Its just that it saves us from
# a kind of overflow problems 


    
    