'''
Question : 

Given an array which consists of one or more zeroes anywhere, what we have to do is write the code so that all the elements other than 
zeroes should be at the beginning and all the zeroes should be at the end, finally return the number of unique elements or zeroes (doesnt matter)

'''

# BruteForce -
# Its simple, take a second array, push all the non zero elements and then from that array, modify the main array elements at 
# the beginning to non zero elements and make rest of the elements to zeroes


#Optimal Approach -
# This is comparatively the best and most efficient solution and the easiest one as well,
# Shame on you for not able to do this in the first try itself

def move_Zeroes(arr):
    l = 0
    for r in range(len(arr)):
        if arr[r] != 0:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    
    return arr

'''
Now let us actually discuss about the types of problems that can be asked based on this exact approach, there may be slight variation but 
the types are :

VARIATION 1 -> You are given an array of integers arr with size n. Your task is to move all the zeroes in the array to the front
    while preserving the relative order of the non - zero elements

HINT => To preserve the order of non-zero elements, iterate from the end and then bring all non zeroes to the end instead of putting zeroes
        at the beginning
        

VARIATION 2 -> You are given an array and an integer target. Our task is to remove all the occurences of the target from the array.
    The elements that are not equal to the target should be moved to the beginning of the array.
    
HINT => Its simple if you think about it, just write the same code and replace the logic of zeroes to match with the target

'''


# My approach - {TC-> O(N) and SC->O(1)}
def move_Zeroes2(arr):
    n = len(arr)
    l,r = 0,0
    
    while r < n:
    
        while l<n and arr[l] != 0:
            l += 1
            
        while r < n:
            if arr[r] != 0 and r > l:
                arr[l], arr[r] = arr[r], arr[l]
                r += 1
                break
            r += 1
        l += 1
    
    return arr,l

ans = move_Zeroes(list(map(int, input().split())))

print(ans)

'''
--------------------------------------------
move_Zeroes(arr) -> Idea of my own approach is down below
--------------------------------------------
Idea:
- Use two pointers: l (left) and r (right).
- 'l' searches for the next zero position.
- 'r' searches for the next non-zero element after 'l'.
- Whenever a non-zero is found at 'r' and l < r,
  swap arr[l] and arr[r], then move both pointers forward.

Key Steps:
1. l starts from 0 and moves until it points to a zero.
2. r moves ahead to find a non-zero element.
3. When found, swap arr[l] and arr[r].
4. Continue until r reaches the end.

This approach modifies the array in-place and keeps track
of the last processed index (returned as 'l').
--------------------------------------------

'''
    