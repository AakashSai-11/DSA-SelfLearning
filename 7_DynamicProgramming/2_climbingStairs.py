'''
So keep in mind that whenever you see something like count number of ways, count occurrences, count all possibilities. It is based
on recursion
'''

# Dynamic Programming Notes – Climbing Stairs (Recursion → Memoization → Tabulation → Space Optimization)

"""
Problem: Climbing Stairs
-----------------------
You are climbing a staircase that has 'n' steps.
Each time, you can take either 1 step or 2 steps.

Question: In how many distinct ways can you reach step 'n'?

Example:
Input : 3
Output: 3
Ways  : [1,1,1], [1,2], [2,1]

This is identical to computing Fibonacci numbers:
f(n) = f(n-1) + f(n-2)
"""


# ------------------------------------------------------------
# 1. Pure Recursion (Exponential Time)
# ------------------------------------------------------------

def climb_recursive(i):
    if i == 0:
        return 1
    if i == 1:
        return 1

    left = climb_recursive(i - 1)
    right = climb_recursive(i - 2)

    return left + right


"""
Explanation:
-----------
Base cases:
- f(0) = 1   (1 way to stand at base)
- f(1) = 1   (1 way to reach first step)

Recursive case:
f(i) = f(i-1) + f(i-2)
→ Last step came from i-1 or i-2.

Complexity:
-----------
Time Complexity  : O(2^n)
Space Complexity : O(n)   (recursion depth)
"""


# ------------------------------------------------------------
# 2. Memoization (Top-Down DP)
# ------------------------------------------------------------

def climb_memo(n, dp):
    if n == 0:
        return 1
    if n == 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = climb_memo(n - 1, dp) + climb_memo(n - 2, dp)
    return dp[n]


"""
Explanation:
-----------
- Use a dp array of size n+1 initialized to -1.
- Store results to avoid repeated calculations.
- Greatly reduces time from O(2^n) → O(n).

Complexity:
-----------
Time Complexity  : O(n)
Space Complexity : O(n)
    - recursion depth + dp array
"""


# ------------------------------------------------------------
# 3. Tabulation (Bottom-Up DP)
# ------------------------------------------------------------

def climb_tab(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


"""
Explanation:
-----------
- Build dp array from 0 → n.
- dp[i] = dp[i-1] + dp[i-2]

Complexity:
-----------
Time Complexity  : O(n)
Space Complexity : O(n)
"""


# ------------------------------------------------------------
# 4. Space-Optimized Tabulation
# ------------------------------------------------------------

def climb_space_opt(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    prev2 = 1   # f(0)
    prev1 = 1   # f(1)

    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


"""
Explanation:
-----------
- Only previous two states are required.
- No need for dp array.

Complexity:
-----------
Time Complexity  : O(n)
Space Complexity : O(1)
"""


"""
------------------------------------------------------------
Climbing Stairs – Summary
------------------------------------------------------------

Method                     Time        Space
------------------------------------------------
Recursive                 O(2^n)      O(n)
Memoization               O(n)        O(n)
Tabulation                O(n)        O(n)
Space-Optimized Tab       O(n)        O(1)

Observations:
------------
- Problem maps directly to Fibonacci.
- DP eliminates exponential redundant calls.
- Space-optimized solution is the best in practice.

------------------------------------------------------------
"""
