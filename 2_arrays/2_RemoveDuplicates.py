'''
Give a sorted array with multiple duplicate values, we have to get the array so that all the elements should be unique and they should be
at the beginning of the array 

The question in a good way is :
Given a sorted integer array arr of size n, your task is to replace the duplicates in-place such that each unique element appears only once,
and the relative order of the elements is preserved. After replacing the duplicates, return the number of unique elements in the array.

- Consider the number of unique elements of arr to be k. To be considered a valid solution, you need to do the following:

    -> Modify the array arr such that the first k elements of arr contain only the unique elements, 
       in the same order they appeared initially.
    -> The remaining elements in arr are irrelevant, as well as the size of arr.
    -> Return k, which is the number of unique elements in arr.

'''

''' Bruteforce way is of converting the list into set or creating the hash set and then replacing the starting elements of the set into
 list '''

 
 # Optimal Approach -> It is based on two pointers
 
def remove_duplicates(arr):
    i,j = 0,1
    
    while j < len(arr):
        if arr[i] != arr[j]:
            arr[i+1] = arr[j]
            i += 1
        j += 1
    
    return arr,i+1



# My approach
def remove_duplicates2(arr):
    n = len(arr)
    ans = 0
    prev = arr[0]
    for i in range(1,n):
        if arr[i] == prev:
            arr[i] = 0
            ans += 1
        else:
            prev = arr[i]
    
    return arr

'''
So basically the solution is divided into two parts : 
Part 1 -> This approach removes the duplicates and replaces them with zeroes
Part 2 -> Now this part deals with moving those zeroes to the end thereby achieving the output, though its a long path, it is still not bad
as the time complexity is optimal
This part 2 is mainly dealt in the next chapter of move zeroes (basically next file), but yeah I am still copying that and pasting it here 
to complete the solution, to understand the below part from here, please read the next file

'''
def move_Zeroes(arr):
    arr = remove_duplicates2(arr)
    n = len(arr)
    l,r = 0,0
    
    while r < n:
    
        while arr[l] != 0 and l<n:
            l += 1
            
        while r < n:
            if arr[r] != 0 and r > l:
                arr[l], arr[r] = arr[r], arr[l]
                r += 1
                break
            r += 1
        l += 1
    
    return arr,l


print(move_Zeroes(list(map(int, input().split()))))
        
        