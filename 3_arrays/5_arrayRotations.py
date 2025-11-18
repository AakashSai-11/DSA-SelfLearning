'''
Rotating the array to the left by 1:

Step 1 : Store first element in temporary variable
Step 2 : Elements from 1st to n-1th index move left by one place
Step 3 : Place temp variable value at last index

TC - O(N) and SC - O(1)
'''

def basic_rotation(arr):
    n = len(arr) - 1
    temp = arr[0]
    for i in range(n):
        arr[i] = arr[i+1]
    arr[n] = temp
    return arr

print(basic_rotation([1,2,5,6,3,4]))

'''
Brute Force -
1. Store the starting k elements into a temporary array
2. Shift the rest elements towards k places
3. Place temporary elements in the array

'''

'''
Optimal Solution -
It is completely mind boggling and think whatever you want but the optimal solution is this way:
1. First reverse first k elements
2. Reverse the next k elements
3. Reverse the entire array
You will fucking get your rotated array to the left by K!!!!

'''

def k_rotations_optimal(arr, k):
    k = k%n
    n = len(arr)
    def reverse(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return
    
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)
    return arr
    
# BLOODY FUCKING GENIUS, YOU SHOULD HAVE BEEN ABLE TO NOTICE THE PATTERN YOU DUMB FUCK !!!!



# My approach - TC is good as it is linear time but we use a dictionary for temporary variable stuff, Its not bad, Its pretty decent
#The idea is basically to finalize the rotations properly by taking the modular division with the length, So we get the optimal rotations
#Once we get the optimal rotations, we basically shift the elements directly by k elements. For the starting k elements we use a 
# dictionary to store the first k elements that we actually use them at the end, so this is the idea basically
# SC -> O(k)
def k_rotations(arr, k):
    n = len(arr)
    d = {}
    k = k%n
    for i in range(k):
        d[i] = arr[i]
    i = 0
    while i + k < n:
        if i+k < n:
            arr[i] = arr[i+k]
        i += 1
    for i in range(k):
        arr[i-k] = d[i]
    return arr

print(k_rotations([1,2,3,4,5,6,7],17))