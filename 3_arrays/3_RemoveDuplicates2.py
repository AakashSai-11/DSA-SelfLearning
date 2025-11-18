'''
This is the extended version of the previous problem of removing the duplicates from the sorted array

Description :-

You are given a sorted array arr in non-decreasing order. Your task is to remove duplicates such that each
unique element appears at most twice.

The output should return the new length k and the array should be updated in-place to have the first k elements without extra duplicates.

Example 1:

Input: arr = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5]

Output:

9
1 1 2 2 3 3 4 5 5
Explanation:

Your function should return k = 9, with the first nine elements of the array being 1, 1, 2, 2, 3, 3, 4, 5, 5 in that order."

'''

def removeDuplicates(arr):
    n = len(arr)
    l,r = 0,0
    while r < n:
        count = 1
        while r+1 < n and arr[r] == arr[r+1]:
            count += 1
            r += 1
            
        for i in range(min(2, count)):
            arr[l] = arr[r]
            l += 1
        r += 1
    
    return arr

print(removeDuplicates(list(map(int, input().split()))))
    