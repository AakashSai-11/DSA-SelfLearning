'''
Question:
----------
Given an array 'nums' and two integers 'left' and 'right', 
find the number of contiguous subarrays such that the 
maximum element in each subarray lies within the range [left, right].

In other words, we want to count all subarrays whose 
maximum value is between left and right (inclusive).

Example:
nums = [2, 1, 4, 3], left = 2, right = 3
Valid subarrays are: [2], [2, 1], [3]
So, the answer is 3.
'''


'''
Approach:
----------
This is a sliding window (two-pointer) approach that efficiently counts
the number of valid subarrays in a single pass.

Key Idea:
- We maintain two pointers:
    i → the start of the current window (after the last element > right)
    j → the current index being processed
- We also keep a variable 'curr' to store the index of the last element 
    that was within the range [left, right].

Logic:
1. If nums[j] > right:
        - Any subarray including nums[j] is invalid.
        - So, we reset the window:
        i = j + 1
        curr = -1

2. If left <= nums[j] <= right:
        - This element is valid and can be the maximum of new subarrays.
        - We update 'curr' = j (the index of the latest valid element)
        - Then, all subarrays ending at j and starting anywhere from i to j 
        are valid.
        Hence, we add (j - i + 1) to our answer.

        WHY (j - i + 1)?
        ----------------
        Suppose our window is from index 'i' to 'j'.
        Example:
            nums = [3, 2, 5]
                    i     j
            left = 2, right = 5

        Here, nums[j] = 5 (valid, since 2 ≤ 5 ≤ 5).

        All possible subarrays ending at j are:
            [5]                → start at j
            [2, 5]             → start at j-1
            [3, 2, 5]          → start at i

        Total = (j - i + 1) subarrays.

        And because nums[j] is within [left, right],
        all of these subarrays will have a maximum value
        that is within [left, right]. So we count all of them.

3. If nums[j] < left:
        - This element alone is too small to be the maximum.
        - However, if we have seen a valid element before (curr != -1),
        then it can extend previous valid subarrays.
        So, we add (curr - i + 1) to the answer.

By the end of the loop, 'ans' holds the total number of valid subarrays.

Time Complexity: O(n)
Space Complexity: O(1)
'''


# I actually managed to do around 90% of the problem but yeah couldnt solve everything, Well I am happy though
def numSubarrayBoundedMax(nums, left, right):
    i,j = 0,0
    curr = -1
    ans = 0
    while j < len(nums):
        if left <= nums[j] <= right:
            curr = j
            ans += j - i + 1
            j += 1
        elif nums[j]<left:
            if curr != -1:
                ans += curr - i + 1
            j += 1
        else:
            i,j = j+1,j+1
            curr = -1
    return ans