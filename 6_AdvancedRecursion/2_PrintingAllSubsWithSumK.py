# Problem: Printing All Subsequences With Sum K

"""
Problem Statement:
Given an array 'arr', print all subsequences whose sum is equal to a target value 'k'.

A subsequence is formed by selecting or skipping elements without changing their order.
We must explore all possible combinations and print only those subsequences whose sum equals k.

Example:
Input: arr = [1, 2, 1], k = 2
Output:
[1, 1]
[2]
"""

# Approach:
# For each element, we have two choices:
#   1. Include the element in the subsequence.
#   2. Exclude the element.
# Maintain the running sum and the current subsequence.
# When index reaches the end, check if the running sum equals k.

def print_subsequences_with_sum_k(i, arr, subseq, current_sum, k):
    n = len(arr)
    
    # Base case: reached end of array
    if i >= n:
        if current_sum == k:
            print(subseq)
        return

    # Pick the current element
    subseq.append(arr[i])
    print_subsequences_with_sum_k(i + 1, arr, subseq, current_sum + arr[i], k)

    # Backtrack: remove the element
    subseq.pop()

    # Not pick the current element
    print_subsequences_with_sum_k(i + 1, arr, subseq, current_sum, k)


# Example Usage:
# print_subsequences_with_sum_k(0, [1, 2, 1], [], 0, 2)


"""
----------------------------------------
Explanation Summary:
----------------------------------------

1. Base Case:
   If i == n:
       - If current_sum == k, print the subsequence.
       - Return since all elements have been considered.

2. Pick Case:
   - Append arr[i] to subseq.
   - Increase current_sum by arr[i].
   - Recurse for the next index (i + 1).

3. Not-Pick Case:
   - Backtrack by removing last element (subseq.pop()).
   - Recurse for the next index (i + 1) without changing current_sum.

4. The recursion explores all combinations exactly like the power set.

----------------------------------------
Time & Space Complexity:
----------------------------------------

Time Complexity: O(2^n * n)
   - 2 choices per element → 2^n subsequences.
   - Printing a valid subsequence costs O(n) in the worst case.
   - Total: O(n * 2^n)

Space Complexity: O(n)
   - Recursion stack depth = n
   - Subsequence storage also up to n
   - Overall: O(n)

----------------------------------------
Summary:
----------------------------------------
- Explore all subsets via include/exclude.
- Print only those subsequences whose sum equals k.
- Classic recursion + backtracking pattern.
----------------------------------------
"""
