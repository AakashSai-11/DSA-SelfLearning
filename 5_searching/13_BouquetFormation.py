# Problem: Bouquet Formation

"""
Problem Statement:
You are given 'n' roses and an array 'arr', where arr[i] represents the day on which the i-th rose blooms.
You must create exactly 'm' bouquets, and each bouquet must consist of 'k' **consecutive** bloomed roses.

Your goal is to determine the minimum number of days required to form at least 'm' bouquets.
If it is not possible to create 'm' bouquets, return -1.

Example:
Input: n = 7, arr = [1, 10, 3, 10, 2, 5, 8], m = 2, k = 3
Output: 8
Explanation:
By day 8, the roses blooming are [1, 3, 2, 5, 8] → we can form 2 bouquets of size 3 consecutively.
"""

# Approach:
# 1. Check if it's even possible to form m bouquets (need n >= m * k).
# 2. Use Binary Search on the range [min(arr), max(arr)] to find the minimum day.
# 3. For each day (mid), count how many bouquets can be made using a helper function.
# 4. Adjust search space:
#    - If enough bouquets can be formed → try smaller day (move left).
#    - Otherwise → move right.
# 5. Return the smallest valid day.

# Helper Function: Calculates how many bouquets can be formed by day 'mid'
def number_of_bouquets(arr, n, k, mid):
    count = 0         # count consecutive bloomed roses
    bouquets = 0      # total bouquets formed

    for i in range(n):
        if arr[i] <= mid:
            count += 1
            if count == k:
                bouquets += 1
                count = 0  # reset for next bouquet
        else:
            count = 0  # reset if rose not bloomed

    return bouquets


# Main Function: Finds the minimum number of days to make at least 'm' bouquets
def min_days_to_form_bouquets(arr, n, k, m):
    # Feasibility check
    if n < m * k:
        return -1

    low = min(arr)
    high = max(arr)
    ans = -1

    # Binary search for minimum valid day
    while low <= high:
        mid = (low + high) // 2
        bouquets = number_of_bouquets(arr, n, k, mid)

        if bouquets >= m:
            ans = mid
            high = mid - 1  # try earlier day
        else:
            low = mid + 1   # need more days

    return ans


# Example Usage:
# arr = [1, 10, 3, 10, 2, 5, 8]
# m = 2
# k = 3
# print(min_days_to_form_bouquets(arr, len(arr), k, m))  # Output: 8


"""
----------------------------------------
Explanation Summary:
----------------------------------------
1. number_of_bouquets(arr, n, k, mid):
   → Iterates through the array.
   → Counts how many consecutive roses are bloomed by day 'mid'.
   → Every 'k' consecutive bloomed roses form one bouquet.
   → Returns the total count of bouquets.

2. min_days_to_form_bouquets(arr, n, k, m):
   → Checks feasibility (if n < m*k → impossible).
   → Uses binary search over days from min(arr) to max(arr).
   → For each day 'mid':
       - Calculates number of bouquets using number_of_bouquets().
       - If enough bouquets are formed, store current 'mid' as possible answer and move left.
       - Otherwise, move right.
   → Returns the earliest day that satisfies the bouquet requirement.

----------------------------------------
Complexity Analysis:
----------------------------------------
Time Complexity: O(n * log(max(arr) - min(arr) + 1))
   → Binary search across day range * O(n) iteration for each check.
Space Complexity: O(1)
   → Only a few variables used.
----------------------------------------
"""
