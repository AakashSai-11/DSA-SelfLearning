# Problem: Monkey Eating Bananas

"""
Problem Statement:
A monkey has 'n' piles of bananas, where the i-th pile has 'a[i]' bananas.
The monkey must finish all the bananas within 'h' hours.

Each hour, the monkey chooses a pile and eats 'm' bananas.
If a pile has fewer than 'm' bananas, the monkey eats all of them and waits for the next hour.

Goal:
Find the minimum integer 'm' (bananas per hour) that allows the monkey to finish within 'h' hours.

Example:
Input: n = 3, a = [3, 9, 6], h = 6
Output: 3

Explanation:
If m = 3:
  - Pile 1 → 3 bananas → 1 hour
  - Pile 2 → 9 bananas → 3 hours
  - Pile 3 → 6 bananas → 2 hours
Total time = 6 hours, so m = 3 is the minimum valid speed.
"""

# Approach:
# 1. Define a helper function to calculate total hours required to eat all bananas at a given speed 'm'.
# 2. Apply Binary Search on the range [1, max(a)] to find the minimum speed that satisfies the time limit 'h'.

import math

# Helper Function: Calculate total hours required at a given eating speed
def time_to_eat(arr, n, m):
    total_time = 0
    for i in range(n):
        total_time += math.ceil(arr[i] / m)
    return total_time


# Main Function: Find minimum eating speed
def min_eating_speed(arr, n, h):
    low = 1
    high = max(arr)
    ans = high  # Initialize with the maximum possible eating speed

    while low <= high:
        mid = (low + high) // 2
        total_time = time_to_eat(arr, n, mid)

        # If monkey can finish within 'h' hours, try smaller speed
        if total_time <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


# Example Usage:
# arr = [3, 9, 6]
# h = 6
# print(min_eating_speed(arr, len(arr), h))  # Output: 3


"""
----------------------------------------
Explanation Summary:
----------------------------------------
1. time_to_eat(arr, n, m):
   → Calculates total hours needed to finish all piles at speed 'm'.
   → Uses ceil(arr[i] / m) for each pile (since monkey may not finish exactly).

2. min_eating_speed(arr, n, h):
   → Binary Search range: [1, max(arr)]
   → For each mid speed:
       - If total_time <= h → possible solution, try smaller speed (move left).
       - Else → too slow, increase speed (move right).
   → Final answer is the smallest 'm' that satisfies the time constraint.

----------------------------------------
Complexity Analysis:
----------------------------------------
Time Complexity: O(n * log(max(arr)))
   → n iterations for time_to_eat per binary search step.
Space Complexity: O(1)
   → Only a few constant variables used.
----------------------------------------

----------------------------------------
Related Problem:
----------------------------------------
There are similar problems based on this concept. 
For example:

You are provided with an array of integers 'arr' and an integer 'limit’.
The task is to find the minimum positive integer divisor such that when 
each element in 'arr' is divided by this divisor, 
the sum of the resulting divisions (taking the ceil of each division) 
does not exceed the given 'limit'.

Example:
If arr = [8, 9, 10] and limit = 7,
Divisor = 3 → ceil(8/3) + ceil(9/3) + ceil(10/3) = 3 + 3 + 4 = 10 (>7)
Divisor = 4 → 2 + 3 + 3 = 8 (>7)
Divisor = 5 → 2 + 2 + 2 = 6 (≤7)
Hence, the answer is 5.
----------------------------------------
"""
