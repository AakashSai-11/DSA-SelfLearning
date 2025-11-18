# Problem: Find Minimum in Rotated Sorted Array

"""
Problem Statement:
Given an array 'arr' of size 'n', sorted in ascending order and rotated between 1 and n times,
find the minimum element in the rotated array.

Example:
Input: arr = [3, 4, 5, 1, 2]
Output: 1
Explanation: The array [1, 2, 3, 4, 5] was rotated 3 times to become [3, 4, 5, 1, 2].
"""

# Approach:
# Use Binary Search to efficiently find the minimum element.
# Check which half (left or right) of the array is sorted.
# Adjust the search range accordingly and track the smallest element.

def minimum(arr):
    n = len(arr)
    low = 0
    high = n-1
    ans = float('inf')
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid+1
        else:
            ans = min(ans, arr[mid])
            high = mid-1
    return ans

print(minimum([4,5,6,2,3]))


# Application: Find Number of Rotations
# The index of the minimum element represents the number of rotations performed.

# Time Complexity: O(log n)
# Space Complexity: O(1)
