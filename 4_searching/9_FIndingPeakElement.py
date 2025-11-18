# Problem: Find Index of Peak Element

"""
Problem Statement:
Given an array 'arr' of length 'n', find the index of a peak element.

A peak element is one that is strictly greater than its neighbors.
That is, for any index 'i':
    arr[i] > arr[i - 1] and arr[i] > arr[i + 1]

If multiple peaks exist, returning the index of any one of them is valid.

Example:
Input: arr = [1, 3, 4, 5, 2]
Output: 3
Explanation: arr[3] = 5 is greater than both arr[2] = 4 and arr[4] = 2.
"""

# Approach:
# 1. Handle base cases (array size 1, first or last element being a peak).
# 2. Use Binary Search to efficiently find a peak:
#    - Compare mid element with its neighbors.
#    - If mid is greater than both → it's a peak.
#    - If mid is increasing towards right → move right.
#    - Else → move left.

def findPeakElement(arr):
    n = len(arr)
    
    # Base cases
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    low, high = 1, n - 2

    while low <= high:
        mid = (low + high) // 2

        # Check if current mid is a peak
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        # If sequence is rising, move right
        elif arr[mid] > arr[mid - 1]:
            low = mid + 1
        # Otherwise, move left
        else:
            high = mid - 1

    return -1  # Should not occur if input has at least one peak


# Time Complexity: O(log n)
# Space Complexity: O(1)

    
print(findPeakElement([1,2,3,4,7,6,5]))

# This code works even in the case of multiple peaks because the answer needs only one peak and that could be any so its fine