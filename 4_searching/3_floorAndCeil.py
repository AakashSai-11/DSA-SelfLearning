"""
----------------------------------------
            FLOOR and CEIL
----------------------------------------

🧩 Problem Statement:
Given a sorted array of integers and an integer x,  
find both the floor and ceiling of x.

Definitions:
- Floor(x) → largest element ≤ x
- Ceil(x)  → smallest element ≥ x

If floor or ceil doesn’t exist, return `None` for that value.

----------------------------------------
🧠 Concept:
We can find both using Binary Search efficiently 
by narrowing down the search space based on comparisons.

----------------------------------------
⚙️ Approach for CEIL:
1️⃣ Initialize:
   - low = 0
   - high = n - 1
   - ceil_val = -1  # holds the smallest element ≥ x

2️⃣ Binary Search Loop:
   while low <= high:
       mid = (low + high) // 2

       if arr[mid] >= x:
           ceil_val = arr[mid]     # potential ceil found
           high = mid - 1          # look for smaller candidate on left
       else:
           low = mid + 1           # move right to find greater element

----------------------------------------
⚙️ Approach for FLOOR:
1️⃣ Initialize:
   - low = 0
   - high = n - 1
   - floor_val = -1  # holds the largest element ≤ x

2️⃣ Binary Search Loop:
   while low <= high:
       mid = (low + high) // 2

       if arr[mid] <= x:
           floor_val = arr[mid]    # potential floor found
           low = mid + 1           # move right to find larger candidate
       else:
           high = mid - 1          # move left to find smaller element

----------------------------------------
💻 Code Implementation:
----------------------------------------
"""


# 🔍 Example Usage:
# arr = [1, 2, 4, 6, 10, 12, 14]
# print(find_floor_and_ceil(arr, 5))   # Output: (4, 6)
# print(find_floor_and_ceil(arr, 1))   # Output: (1, 1)
# print(find_floor_and_ceil(arr, 15))  # Output: (14, -1)
# print(find_floor_and_ceil(arr, 0))   # Output: (-1, 1)

"""
----------------------------------------
📚 Summary:
----------------------------------------
FLOOR(x) → largest value ≤ x  
CEIL(x)  → smallest value ≥ x  

Both can be found in O(log n) using Binary Search.
----------------------------------------
"""

def floor(arr, x):
    n = len(arr)
    low = 0
    high = n-1
    ans = -1
    
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans

print(floor([5,5,10,10,15,15,25],30))


def ceil(arr, x):
    n = len(arr)
    low = 0
    high = n-1
    ans = -1
    
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

print(ceil([5,5,10,10,15,15,25],30))