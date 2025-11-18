# Problem: Find the Single Non-Repeating Element in a Sorted Array

"""
Problem Statement:
Given a sorted array 'arr' of size 'n' where every element appears exactly twice 
except for one unique element that appears only once, 
find and return that single non-repeating element.

Example:
Input: arr = [1, 1, 2, 3, 3, 4, 4]
Output: 2
Explanation: Every element appears twice except for 2, which appears once.
"""

# Approach:
# 1. Handle base cases directly for arrays of size 1 or where the unique element is at the start or end.
# 2. Use Binary Search for efficiency:
#    - Check if mid element is the unique one.
#    - Use the index parity pattern (even/odd) to decide which half to continue searching in.


def findSingleElement(arr):
    # Base cases
    if len(arr) == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[-2]:
        return arr[-1]
    low = 1
    high = len(arr)-2
    
    while low <= high:
        mid = low + (high - low)//2
        
         # Check if mid is the unique element
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        
        # Pattern logic:
        # If index is even and element matches with next => unique element is on the right
        # If index is odd and element matches with previous => unique element is on the right
        elif (mid%2 == 0 and arr[mid] == arr[mid+1]) or (mid%2==1 and arr[mid] == arr[mid-1]):
            low = mid + 1
        elif (mid % 2 == 0 and arr[mid] == arr[mid-1]) or (mid%2==1 and arr[mid] == arr[mid+1]):
            high = mid - 1
    

print(findSingleElement([1,1,2,2,4,5,5,6,6,7,7]))

# Time Complexity: O(log n)
# Space Complexity: O(1)