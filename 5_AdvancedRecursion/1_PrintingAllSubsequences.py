# Problem: Printing All Subsequences using Recursion

"""
Problem Statement:
Given an array, print all possible subsequences using recursion.

A subsequence of an array is a sequence that can be derived by 
deleting zero or more elements without changing the order of the remaining elements.

Example:
Input: [4, 5, 6]
Output:
[]
[6]
[5]
[5, 6]
[4]
[4, 6]
[4, 5]
[4, 5, 6]
(→ Total 2^n subsequences)
"""

# Approach:
# For every element, we have 2 choices:
# 1. Include the element in the subsequence.
# 2. Exclude the element and move to the next.
# This forms a binary recursion tree of depth n, covering all 2^n combinations.


# ------------------------------------------------------------
# METHOD 1: Using new list creation on every recursion call
# ------------------------------------------------------------

def subsequence(arr, main, index):
    if index >= len(main):
        print(arr)
        return
    
    # Include the current element
    subsequence(arr + [main[index]], main, index + 1)

    # Exclude the current element
    subsequence(arr, main, index + 1)


# ------------------------------------------------------------
# METHOD 2: Using in-place modification (append / pop)
# ------------------------------------------------------------

def subsequence_2(arr, main, index):
    if index >= len(main):
        print(arr)
        return
    
    # Include current element
    arr.append(main[index])
    subsequence_2(arr, main, index + 1)

    # Backtrack (remove last element)
    arr.pop()

    # Exclude current element
    subsequence_2(arr, main, index + 1)


# Example Usage:
# subsequence_2([], [4, 5, 6], 0)


"""
----------------------------------------
Explanation:
----------------------------------------

1️⃣ Base Case:
   If index == len(main):
       → All elements have been considered.
       → Print the current subsequence (arr).

2️⃣ Recursive Case:
   For each index, we make two recursive calls:
       → Include arr[index] in subsequence.
       → Exclude arr[index] from subsequence.

3️⃣ Backtracking (Method 2 only):
   - When using append/pop, we modify the same list (arr) in-place.
   - Before returning to the previous recursive level, we 'pop' the last element to restore the state.

----------------------------------------
Comparison Between Methods:
----------------------------------------

| Feature             | Method 1                          | Method 2                        |
|---------------------|-----------------------------------|----------------------------------|
| Memory Usage        | Creates a new list every call     | Uses same list via append/pop   |
| Performance         | Slightly slower (extra copying)   | More efficient (in-place ops)   |
| Code Simplicity     | Simpler to understand             | Requires careful backtracking   |
| Preferred Approach  | ❌ Less optimal                    | ✅ Better for larger inputs      |

**Hence, Method 2 (append + pop) is the preferred approach** 
for space efficiency and reduced list-copying overhead.

----------------------------------------
Time & Space Complexity:
----------------------------------------

Let n = length of array

Time Complexity:
→ Each element has 2 choices → Total 2^n subsequences
→ Printing each subsequence takes O(n) time in the worst case
Overall Time = O(n * 2^n)

Space Complexity:
→ Recursion depth = O(n)
→ Auxiliary space (Method 1): O(n * 2^n) due to new list copies
→ Auxiliary space (Method 2): O(n) for recursion + O(n) for current subsequence
Overall Space (preferred method) = O(n)

----------------------------------------
Summary:
----------------------------------------
- Both methods explore all inclusion/exclusion possibilities.
- Method 1 → simpler but less memory-efficient.
- Method 2 → efficient and clean using backtracking.
- Total subsequences generated = 2^n
----------------------------------------
"""
