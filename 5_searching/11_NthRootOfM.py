# Problem: Find the Nth Root of M

"""
Problem Statement:
Given two positive integers 'n' and 'm', find the integer value of the nth root of m (n√m).

If there exists an integer 'x' such that x^n = m, return x.
Otherwise, return -1.

Example:
Input: n = 3, m = 27
Output: 3
Explanation: 3^3 = 27, so 3 is the cube root of 27.

Input: n = 2, m = 10
Output: -1
Explanation: √10 is not an integer.
"""

# Approach:
# Use Binary Search on the range [1, m] to efficiently find integer 'x' such that x^n = m.
# Handle large values carefully by checking for overflow during power calculation.

# Helper Function: Computes mid^n and checks its relation with m
def power(mid, n, m):
    ans = 1
    for _ in range(n):
        ans *= mid
        # If at any point ans exceeds m, no need to continue — it’s too large
        if ans > m:
            return 1  # mid^n > m
    if ans == m:
        return 0      # mid^n == m
    return -1         # mid^n < m


# Main Function: Finds the nth root of m
def nthRoot(n, m):
    low, high = 1, m

    while low <= high:
        mid = (low + high) // 2
        result = power(mid, n, m)

        if result == 0:
            return mid  # Found exact nth root
        elif result == -1:
            low = mid + 1  # mid^n < m → move right
        else:
            high = mid - 1  # mid^n > m → move left

    return -1  # No integer nth root found


# Example Usage:
# print(nthRoot(3, 27))  # Output: 3
# print(nthRoot(2, 10))  # Output: -1


# Time Complexity: O(log m * n)
#    → Binary search runs in O(log m)
#    → Power function runs in O(n) per iteration
# Space Complexity: O(1)
