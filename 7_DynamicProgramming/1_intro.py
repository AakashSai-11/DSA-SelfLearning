# Dynamic Programming Notes – Fibonacci (Recursion, Memoization, Tabulation, Space Optimization)

"""
Introduction to Dynamic Programming
-----------------------------------
Dynamic Programming (DP) improves inefficient recursive solutions by storing
and reusing results of subproblems.

Many recursive problems (like Fibonacci) recompute the same values repeatedly.
DP reduces such exponential time complexity to linear or polynomial time.


------------------------------------------------------------
1. Recursive Fibonacci (No DP)
------------------------------------------------------------
Definition:
Fib(n) = Fib(n-1) + Fib(n-2)

Base cases:
Fib(0) = 0
Fib(1) = 1

This uses a recursion tree and recomputes many values repeatedly.
"""


# Pure Recursion (Exponential Time)
def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)


"""
Complexity:
Time Complexity  : O(2^n)
Space Complexity : O(n)  (recursion depth)

------------------------------------------------------------
2. Memoization (Top-Down DP)
------------------------------------------------------------
Memoization stores already computed Fibonacci values in an array/dict.

Approach:
- Create dp array of size n+1 with all values initialized to -1.
- If dp[n] already computed → return it.
- Otherwise compute recursively and store it in dp[n].
"""


def fib_memo(n, dp):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib_memo(n-1, dp) + fib_memo(n-2, dp)
    return dp[n]


"""
Complexity:
Time Complexity  : O(n)
Space Complexity : O(n)
   - Recursion depth = n
   - dp array size    = n+1

Memoization avoids recomputation by storing results once.

------------------------------------------------------------
3. Tabulation (Bottom-Up DP)
------------------------------------------------------------
Build dp array from 0 → n iteratively.

Approach:
- Create dp of size n+1
- dp[0] = 0
- dp[1] = 1
- Loop i from 2..n:
      dp[i] = dp[i-1] + dp[i-2]
"""


def fib_tab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


"""
Complexity:
Time Complexity  : O(n)
Space Complexity : O(n)

Tabulation avoids recursion entirely and builds the solution bottom-up.

------------------------------------------------------------
4. Space Optimized Tabulation
------------------------------------------------------------
To compute Fib(n), only the last two Fibonacci values are needed.

Approach:
- Use two variables (prev2, prev1)
- Iterate from 2..n:
      curr = prev1 + prev2
      prev2 = prev1
      prev1 = curr
"""


def fib_space_opt(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev2 = 0   # Fib(0)
    prev1 = 1   # Fib(1)

    for _ in range(2, n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


"""
Complexity:
Time Complexity  : O(n)
Space Complexity : O(1)

Uses only constant space and is the most efficient standard approach.

------------------------------------------------------------
COMPLEXITY COMPARISON
------------------------------------------------------------

Method                     Time        Space
------------------------------------------------
Recursive (No DP)          O(2^n)      O(n)
Memoization                O(n)        O(n)
Tabulation                 O(n)        O(n)
Space Optimized Tab        O(n)        O(1)

------------------------------------------------------------
Summary:
- Recursion is simplest but too slow.
- Memoization fixes recursion by caching.
- Tabulation is fully iterative and avoids recursion.
- Space-optimized tabulation is the most efficient implementation.
------------------------------------------------------------
"""
