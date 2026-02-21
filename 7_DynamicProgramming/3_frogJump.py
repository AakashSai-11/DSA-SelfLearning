# Dynamic Programming Notes – Frog Jump (Recursion → Memoization → Tabulation → Space Optimization)

"""
Problem: Frog Jump
------------------
You are given 'n' stairs, each with a certain height.
The frog starts at stair 0 and wants to reach stair n-1.

From stair i, the frog can jump to:
- i + 1
- i + 2

Energy cost for jumping from stair i → j is:
    abs(height[i] - height[j])

Goal:
Find the **minimum total energy** required to reach stair n-1.

This is a classic DP problem similar to climbing stairs,
but with height differences added as cost.
"""


# ------------------------------------------------------------
# 1. Pure Recursion (Exponential Time)
# ------------------------------------------------------------

def frog_recursive(i, height):
    if i == 0:
        return 0
    if i == 1:
        return abs(height[1] - height[0])

    s1 = abs(height[i] - height[i - 1]) + frog_recursive(i - 1, height)
    s2 = abs(height[i] - height[i - 2]) + frog_recursive(i - 2, height)

    return min(s1, s2)


"""
Explanation:
-----------
Base cases:
- i == 0 → cost = 0 (starting point)
- i == 1 → cost = |height[1] - height[0]|

Recursive step:
To reach stair i:
    Option 1: jump from i-1 → cost = |hi - h(i-1)| + cost(i-1)
    Option 2: jump from i-2 → cost = |hi - h(i-2)| + cost(i-2)

Take the minimum.

Complexity:
-----------
Time Complexity  : O(2^n)
Space Complexity : O(n)
"""


# ------------------------------------------------------------
# 2. Memoization (Top-Down DP)
# ------------------------------------------------------------

def frog_memo(i, height, dp):
    if i == 0:
        return 0
    if i == 1:
        return abs(height[1] - height[0])

    if dp[i] != -1:
        return dp[i]

    s1 = abs(height[i] - height[i - 1]) + frog_memo(i - 1, height, dp)
    s2 = abs(height[i] - height[i - 2]) + frog_memo(i - 2, height, dp)

    dp[i] = min(s1, s2)
    return dp[i]


"""
Explanation:
-----------
- dp[i] stores the minimum energy required to reach stair i.
- If dp[i] already computed → return it.
- Otherwise compute recursively, store, and return.

Complexity:
-----------
Time Complexity  : O(n)
Space Complexity : O(n)   (dp array + recursion stack)
"""


# ------------------------------------------------------------
# 3. Tabulation (Bottom-Up DP)
# ------------------------------------------------------------

def frog_tab(height):
    n = len(height)
    if n == 1:
        return 0

    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(height[1] - height[0])

    for i in range(2, n):
        s1 = abs(height[i] - height[i - 1]) + dp[i - 1]
        s2 = abs(height[i] - height[i - 2]) + dp[i - 2]
        dp[i] = min(s1, s2)

    return dp[-1]


"""
Explanation:
-----------
- Bottom-up iteration fills dp[i] using previous values.
- dp[i] = min( cost from i-1 , cost from i-2 )

Complexity:
-----------
Time Complexity  : O(n)
Space Complexity : O(n)
"""


# ------------------------------------------------------------
# 4. Space-Optimized Tabulation
# ------------------------------------------------------------

def frog_space_opt(height):
    n = len(height)
    if n == 1:
        return 0

    prev2 = 0                       # dp[i-2]
    prev1 = abs(height[1] - height[0])  # dp[i-1]

    for i in range(2, n):
        s1 = abs(height[i] - height[i - 1]) + prev1
        s2 = abs(height[i] - height[i - 2]) + prev2
        curr = min(s1, s2)

        # shift window forward
        prev2 = prev1
        prev1 = curr

    return prev1


"""
Explanation:
-----------
- Only two previous dp values are required at a time.
- Eliminates the need for entire dp array.

Complexity:
-----------
Time Complexity  : O(n)
Space Complexity : O(1)
"""


"""
------------------------------------------------------------
Frog Jump – Complete Summary
------------------------------------------------------------

Method                     Time        Space
------------------------------------------------
Recursive                 O(2^n)      O(n)
Memoization               O(n)        O(n)
Tabulation                O(n)        O(n)
Space-Optimized Tab       O(n)        O(1)

Observations:
------------
- Problem is equivalent to computing minimum path cost with limited moves.
- Recursion explores all paths → exponential.
- DP eliminates repeated work by storing subproblem answers.
- Space optimization reduces memory usage drastically.

This is the standard DP pattern:
    1. Define subproblem in terms of index.
    2. Explore all allowed moves.
    3. Pick the minimum cost move.
------------------------------------------------------------
"""
