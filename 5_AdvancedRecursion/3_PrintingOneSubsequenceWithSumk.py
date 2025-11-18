# Problem: Printing Only One Subsequence With Sum = K

"""
Problem Statement:
Given an array 'arr' and a target sum 'k', print **any one** subsequence whose
elements sum to exactly 'k' using recursion.

Unlike the full-subsequence problem, this stops as soon as one valid subsequence is found.

Example:
Input: arr = [4, 5, 6], k = 9
Output: [4, 5]
"""


# Approach:
# - For each element, choose between:
#       1. Pick it → add to subsequence and increase sum.
#       2. Not pick → skip it.
# - Recursively explore both possibilities.
# - When index reaches end, check if current_sum == k:
#       → If yes, print the subsequence and return True.
# - Return True upward as soon as one valid subsequence is found.
# - This stops further recursion immediately after finding one valid answer.

def one_subsequence_with_sum_k(i, arr, subseq, current_sum, k):
    n = len(arr)

    # Base case: end of array reached
    if i >= n:
        if current_sum == k:
            print(subseq)
            return True
        return False

    # Pick case
    subseq.append(arr[i])
    if one_subsequence_with_sum_k(i + 1, arr, subseq, current_sum + arr[i], k):
        return True

    # Backtrack: undo the pick
    subseq.pop()

    # Not pick case
    if one_subsequence_with_sum_k(i + 1, arr, subseq, current_sum, k):
        return True

    # Neither pick nor not pick found a valid subsequence
    return False


# Example Usage:
# one_subsequence_with_sum_k(0, [4, 5, 6], [], 0, 9)


"""
----------------------------------------
Explanation Summary:
----------------------------------------

1. Base Case:
   If i == n:
       - Check if current_sum equals target k.
       - If yes → print subseq and return True.
       - Else → return False.

2. Pick the element:
   - Append arr[i] to subseq.
   - Add arr[i] to current_sum.
   - Recurse on next index.
   - If this returns True → propagate True to stop further search.

3. Backtrack:
   - Remove arr[i] from subseq before exploring the not-pick branch.

4. Not Pick the element:
   - Leave subseq unchanged.
   - Recurse to next index.
   - If True → propagate upward.

5. If neither branch finds a valid subsequence, return False.

----------------------------------------
Time & Space Complexity:
----------------------------------------

Time Complexity:
Worst case: O(2^n)
   - In the worst case, no subsequence equals k until the last branch.
   - But unlike printing all subsequences (which is O(n * 2^n)), 
     this stops early once a solution is found.

Space Complexity: O(n)
   - Recursion depth = n
   - Subsequence list uses at most n elements.
   - Total auxiliary space = O(n)

----------------------------------------
Summary:
----------------------------------------
- Explore include/exclude choices.
- Stop immediately when one valid subsequence is found.
- Uses backtracking to maintain subsequence state.
----------------------------------------
"""
