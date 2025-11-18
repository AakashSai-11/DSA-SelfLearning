'''
──────────────────────────────────────────────────────────────────────────────
🧠 Aggressive Cows — Binary Search on Answer (Notes)
──────────────────────────────────────────────────────────────────────────────

🔹 Problem Essence
We are given stall positions and need to place 'c' cows in them.
Goal → maximize the minimum distance between any two cows.

This is not binary search on the array itself.
This is binary search on the **answer space** (possible distances).

──────────────────────────────────────────────────────────────────────────────
🔹 Key Insight — “Maximize the Minimum” Problems
This problem falls under:
    → maximize the minimum distance / minimize maximum load / etc.

The rule:
    If mid (a candidate minimum distance) is possible,
        try for a larger value → low = mid + 1
    else
        reduce the value → high = mid - 1

This pattern is universal for:
- Aggressive Cows
- Allocate Books
- Painter’s Partition
- Router Placement
- Similar threshold-search problems

──────────────────────────────────────────────────────────────────────────────
🔹 Steps

1. Sort stall positions.
   Mandatory. Greedy placement fails without sorting.

2. Define search space for distances:
        low  = 1
        high = arr[n-1] - arr[0]
   We search for the distance, not the index.

3. Feasibility check (can we place all cows?):
   - Place first cow at arr[0]
   - For every next stall:
         if current_stall - last_placed >= mid:
             place cow there
   - If we placed >= c cows → mid is feasible.
   - The code could be like this :
   
'''
c = 1 # No of Cows
def getResult(arr,k):
    prev = -1
    total = 0
    arr.sort()
    for i in arr:
        if prev < 0:
            prev = i
            total += 1
            if total == c:
                return 1
        else:
            if i - prev >= k:
                prev = i
                total += 1
                if total == c:
                    return 1
            else:
                continue
    return -1
    
'''
4. Binary Search Logic:
        while low <= high:
            mid = (low + high) // 2
            if feasible(mid):
                ans = mid
                low = mid + 1      # try to maximize the minimum
            else:
                high = mid - 1

5. Final answer is stored in 'ans'.

──────────────────────────────────────────────────────────────────────────────
🔹 Things to Always Remember
- Sort the stalls.
- Think in terms of **distance**, not positions.
- Feasibility check = greedy placement.
- Pattern for “max of min” targets:
        if feasible → low = mid + 1
        else        → high = mid - 1
- Answer = largest feasible minimum distance.

──────────────────────────────────────────────────────────────────────────────
'''