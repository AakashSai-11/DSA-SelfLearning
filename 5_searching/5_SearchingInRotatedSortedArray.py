"""
----------------------------------------
        SEARCH IN ROTATED SORTED ARRAY
----------------------------------------

🧩 Problem Statement:
You are given a **sorted array** `arr` of size `n`, which has been **rotated**
at an unknown pivot.  
You must find the **index** of a given element `k` in this rotated array.

If `k` is not found → return `-1`.

Example:
Original array: [2, 4, 6, 7, 8]
After rotation at index 3 → [7, 8, 2, 4, 6]
If k = 4 → Output = 3

----------------------------------------
🧠 Concept:
The rotated sorted array still maintains **sorted order** in one of its halves.  
Using **Binary Search**, we can:
1️⃣ Identify which half (left or right) is sorted.
2️⃣ Check if `k` lies in that sorted half.
3️⃣ Narrow the search space accordingly.

----------------------------------------
⚙️ Algorithm Explanation
----------------------------------------

1️⃣ Initialization:
   - low = 0
   - high = n - 1

2️⃣ Binary Search Loop:
   while low <= high:
       - mid = (low + high) // 2

       - If arr[mid] == k:
           → return mid   # element found

3️⃣ Check Which Half is Sorted:
   - If left half is sorted:
       (arr[low] <= arr[mid])
       → Then check if k lies between arr[low] and arr[mid]
         - If yes:  high = mid - 1  (search left half)
         - Else:    low = mid + 1   (search right half)

   - Else (right half is sorted):
       (arr[mid] <= arr[high])
       → Then check if k lies between arr[mid] and arr[high]
         - If yes:  low = mid + 1   (search right half)
         - Else:    high = mid - 1  (search left half)

4️⃣ Termination:
   - If the loop ends without finding the element → return -1

----------------------------------------
💻 Code Implementation:
----------------------------------------
"""

def search_in_rotated_sorted_array(arr, k):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        # ✅ Step 1: Check if found
        if arr[mid] == k:
            return mid

        # ✅ Step 2: Check if left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # ✅ Step 3: Otherwise, right half is sorted
        elif arr[mid] <= arr[high]:
            if arr[mid] < k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    # Element not found
    return -1


# 🔍 Example Usage:
# arr = [7, 8, 2, 4, 6]
# print(search_in_rotated_sorted_array(arr, 4))  # Output: 3
# print(search_in_rotated_sorted_array(arr, 7))  # Output: 0
# print(search_in_rotated_sorted_array(arr, 10)) # Output: -1

"""
----------------------------------------
📚 Summary:
----------------------------------------
- One half of the rotated array is always sorted.
- Use binary search logic to decide which half to search next.
- Time Complexity → O(log n)
- Space Complexity → O(1)
----------------------------------------

-> REMEMBER THAT THIS WORKS ONLY FOR ARRAYS WITHOUT ANY DUPLICATES THAT MEANS, UNIQUE ELEMENTS ARE THERE IN THE ARRAY

"""