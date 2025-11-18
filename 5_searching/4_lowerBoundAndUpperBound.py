'''
----------------------------------------
            LOWER BOUND
----------------------------------------

🧩 Problem Statement:
Given a sorted array `arr` and a number `x`, 
find the index of the **lower bound** of `x` in `arr`.

The **lower bound** of `x` is defined as:
→ the smallest index `i` such that `arr[i] >= x`

If all elements are smaller than `x`, 
then the lower bound is considered to be `n` (size of the array).

----------------------------------------
🧠 Algorithm Explanation (Binary Search Approach)
----------------------------------------

1️⃣ Initialization:
   - low = 0
   - high = n - 1
   - ans = n   // assume no element >= x initially

2️⃣ Binary Search Loop:
   while (low <= high):
       - mid = (low + high) / 2

       if (arr[mid] >= x):
           ans = mid       // potential lower bound
           high = mid - 1  // move left to find smaller index
       else:
           low = mid + 1   // move right since arr[mid] < x

3️⃣ Termination:
   - Loop stops when low > high
   - `ans` holds the index of the lower bound

----------------------------------------
🧾 Example:
arr = [1, 2, 4, 6, 8, 10], x = 5
→ lower_bound = index 2 (since arr[2] = 4 < 5, arr[3] = 6 ≥ 5)



----------------------------------------
            UPPER BOUND
----------------------------------------

🧩 Problem Statement:
Given a non-decreasingly sorted array `arr` and a number `x`,
find the index of the **upper bound** of `x` in `arr`.

The **upper bound** of `x` is defined as:
→ the smallest index `i` such that `arr[i] > x`

If all elements are ≤ x, 
then the upper bound is considered to be `n` (size of the array).

----------------------------------------
🧠 Algorithm Explanation (Binary Search Approach)
----------------------------------------

1️⃣ Initialization:
   - low = 0
   - high = n - 1
   - ans = n   // assume no element > x initially

2️⃣ Binary Search Loop:
   while (low <= high):
       - mid = (low + high) / 2

       if (arr[mid] > x):
           ans = mid;       // potential upper bound
           high = mid - 1;  // move left to find smaller index
       else:
           low = mid + 1;   // move right since arr[mid] <= x

3️⃣ Termination:
   - Loop stops when low > high
   - `ans` holds the index of the upper bound

----------------------------------------
🧾 Example:
arr = [1, 2, 4, 6, 8, 10], x = 6
→ upper_bound = index 4 (since arr[3] = 6 ≤ 6, arr[4] = 8 > 6)


----------------------------------------
📚 Summary:
----------------------------------------
Lower Bound → first index where arr[i] >= x  
Upper Bound → first index where arr[i] > x
----------------------------------------
'''

def lowerBound(arr, target):
    ans = len(arr)
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

print(lowerBound([1,2,3,4,5,6], 5))
# There is a direct inbuilt function for this in c++ which is called lower_bound(arr, arr+n, x)
# For python this is bisect_left(arr, x) -> Gives the index of the lower bound


def upperBound(arr, target):
    ans = len(arr)
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
print(upperBound([1,2,3,4,5,6],5))
# There is an inbuilt function for this as well which is upper_bound(arr, arr+n, x)
# For python, it is 

# Ofcourse the TC is O(logn) and SC is O(1)

# => Applications of lowerBound :

"""
----------------------------------------
        SEARCH INSERT POSITION
----------------------------------------

🧩 Problem Statement:
Given a **sorted array** containing distinct values and a **target value**,  
find the index of the target in the array.

- If the target exists → return its index.
- If not found → return the index where it should be **inserted** 
  to maintain sorted order.

This problem is logically identical to finding the **Lower Bound**.

----------------------------------------
🧠 Algorithm Explanation (Binary Search Approach)
----------------------------------------

1️⃣ Initialization:
   - low = 0
   - high = n - 1
   - ans = n   # assume target is greater than all elements initially

2️⃣ Binary Search Loop:
   while low <= high:
       mid = (low + high) // 2

       if arr[mid] >= target:
           ans = mid         # potential position to insert target
           high = mid - 1    # check if target can go earlier
       else:
           low = mid + 1     # move right to find suitable position

3️⃣ Termination:
   - When the loop ends, `ans` holds:
     → index of the target (if found)
     → or position where target should be inserted.

----------------------------------------
🧾 Example:
arr = [1, 3, 5, 6], target = 5
→ Output: 2 (since arr[2] = 5)

arr = [1, 3, 5, 6], target = 2
→ Output: 1 (insert before 3 to keep array sorted)

arr = [1, 3, 5, 6], target = 7
→ Output: 4 (insert at end)


# 🔍 Example usage:
# print(search_insert_position([1, 3, 5, 6], 5))  # Output: 2
# print(search_insert_position([1, 3, 5, 6], 2))  # Output: 1
# print(search_insert_position([1, 3, 5, 6], 7))  # Output: 4

----------------------------------------
📚 Summary:
----------------------------------------
- This is the same logic as the **Lower Bound**.
- Finds exact index if present, else insertion position.
----------------------------------------
"""
