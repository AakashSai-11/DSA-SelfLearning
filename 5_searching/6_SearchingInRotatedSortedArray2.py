"""
----------------------------------------
     SEARCH IN ROTATED SORTED ARRAY (WITH DUPLICATES)
----------------------------------------

-> Problem Statement:
You are given a **rotated sorted array** `a` of length `n`, possibly containing **duplicates**,
and an integer `k`.

Determine whether `k` exists in the array.

If found → return True  
If not found → return False

Example:
Original array: [4, 5, 6, 7, 8, 9, 9]
Rotated at index 3 → [7, 8, 9, 9, 4, 5, 6]
If k = 5 → Output: True

----------------------------------------
🧠 Concept:
This is an extension of the standard rotated sorted search problem.  
Duplicates make it harder to identify which half is sorted.  
Hence, an additional step is added when:
    arr[low] == arr[mid] == arr[high]
In this case, move both pointers inward to shrink the range.

----------------------------------------
⚙️ Algorithm Explanation:
----------------------------------------

1️⃣ Initialization:
   - low = 0
   - high = n - 1

2️⃣ Binary Search Loop:
   while low <= high:
       mid = (low + high) // 2

       - If arr[mid] == k:
           return True

       - Handle duplicates:
           if arr[low] == arr[mid] == arr[high]:
               low += 1
               high -= 1
               continue

       - Check if left half is sorted:
           if arr[low] <= arr[mid]:
               if arr[low] <= k < arr[mid]:
                   high = mid - 1
               else:
                   low = mid + 1

       - Else, right half is sorted:
           else:
               if arr[mid] < k <= arr[high]:
                   low = mid + 1
               else:
                   high = mid - 1

3️⃣ Termination:
   - If loop ends, element not found → return False

----------------------------------------
💻 Code Implementation:
----------------------------------------
"""

def search_in_rotated_sorted_array_with_duplicates(arr, k):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            return True

        # Handle duplicates (ambiguous case)
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        # Left half sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half sorted
        else:
            if arr[mid] < k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


# 🔍 Example Usage:
# arr = [7, 8, 9, 9, 4, 5, 6]
# print(search_in_rotated_sorted_array_with_duplicates(arr, 5))  # Output: True
# print(search_in_rotated_sorted_array_with_duplicates(arr, 10)) # Output: False

"""
----------------------------------------
📚 Summary:
----------------------------------------
- Works for rotated arrays with duplicates.
- Key ambiguity arises when arr[low] == arr[mid] == arr[high].
- Time Complexity: O(log n) in general, but may degrade to O(n) in worst case (due to duplicates).
- Space Complexity: O(1)
----------------------------------------
"""
