'''
We have to basically find the first and last occurence of a number in an array, If the element is not present in the array
Return -1 for both the occurences
'''

def bruteforce(arr, x):
    first = -1
    last = -1
    for i,e in enumerate(arr):
        if e == x:
            if first == -1:
                first = i
            last = i
    
    return first, last

print(bruteforce([1,2,3,3,3,4,5],3))
# Its good but we have to do this in logn time

# Optimal:

def firstOccurence(arr, x):
    first = -1
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return first

def lastOccurence(arr, x):
    last = -1
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low+(high-low)//2
        
        if arr[mid] == x:
            last = mid
            low = mid+1
        elif arr[mid] > x:
            high = mid-1
        else:
            low = mid+1
            
    return last

print(firstOccurence([1,2,3,3,3,4,5],4))
print(lastOccurence([1,2,3,3,3,4,5],4))

# Its simple actually, We are using two binary searches to find the each one, Its straight forward, Look at the code and you will
# Understand it easily

'''
Application of the above problem:

=> Find the number of occurences of an element in the sorted array, and to do this in logn time, This is the only way

1. First find the first occurence of the number
2. Then find the last occurence of the number
3. Do last - first + 1, We get out answer
4. Just Do one optimisation for no occurence case as both first and last will be -1, Just add an if

'''