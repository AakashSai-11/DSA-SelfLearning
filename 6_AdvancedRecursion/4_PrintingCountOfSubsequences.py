# Problem: Counting Subsequences With Sum = K

"""
Problem Statement:
Given an array 'arr' of length 'n' and a target sum 'k',
count how many subsequences of the array have a sum equal to 'k'.

Example:
Input: arr = [4, 5, 9], k = 9
Valid subsequences → [9], [4, 5]
Output: 2
"""

# Approach:
# - Recursively explore every element with two choices:
#       1. Pick it  → add to current sum.
#       2. Not pick → skip it.
# - When the index reaches n, check if accumulated sum == k.
# - Instead of printing subsequences, return counts:
#       pick_count + not_pick_count
# - This explores the entire power set → full recursion tree.


def count_subsequences_with_sum_k(i, arr, current_sum, k):

    # Base case: all elements processed
    if i >= len(arr):
        if current_sum == k:
            return 1
        return 0

    # Pick the current element
    left = count_subsequences_with_sum_k(i + 1, arr, current_sum + arr[i], k)

    # Not pick the current element
    right = count_subsequences_with_sum_k(i + 1, arr, current_sum, k)

    return left + right


# Example Usage:
# print(count_subsequences_with_sum_k(0, [4, 5, 9], 0, 9))  # Output: 2


"""
----------------------------------------
Explanation Summary:
----------------------------------------

1. Base Case:
   When i == n:
       - If current_sum == k → return 1 (valid subsequence)
       - Else → return 0

2. Pick Case:
   - Add arr[i] to current_sum.
   - Recurse to next index.
   - Store result as left.

3. Not Pick Case:
   - Do not modify current_sum.
   - Recurse to next index.
   - Store result as right.

4. Return:
   left + right → total subsequences whose sum equals k.

----------------------------------------
Time & Space Complexity:
----------------------------------------

Time Complexity: O(2^n)
   - Each element has 2 choices: pick / not pick → full power set explored.
   - No printing, so no extra O(n) factor.
   - Total: O(2^n)

Space Complexity: O(n)
   - Maximum recursion depth = n.
   - No extra space besides function call stack.

----------------------------------------
Summary:
----------------------------------------
- Standard include/exclude recursion.
- Count returned instead of printing subsequences.
- Full exploration → 2^n calls.
----------------------------------------
"""
