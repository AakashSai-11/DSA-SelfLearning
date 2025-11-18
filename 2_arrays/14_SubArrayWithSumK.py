'''
So the question basically means that we have to find the longest Sub array with sum K, Sub Array represents a part of array, Ofcourse
meaning that it is continuous, Understanding this with an example

Let arr = [1, 4, 1, 3, 1, 1, 2, 1, 2]
For this array, The [4, 1, 3] array is a sub array, [1, 3] is a sub array too but arrays like [3, 2] aren't. I think you understood the 
gist of it, Basically the continguous parts of the array are the sub arrays, These parts can be anywhere in the array but they should be 
continguous.
-> Entire array can be the sub array to itself as well.

Now coming back to the question, We have to find the longest sub array with sum k, Taking the above example itself if the k = 5,
Considering the subarray [4, 1] -> This is the subarray and sum = 5, Satisfies the conditions and the length of this subarray is 2
For [3, 1, 1] -> Sum is 5 and length is 3
Similarly we have to consider all possible sub arrays and then return the longest sub array we can get in the entire array


=> It seems that this question is further divided into two types or parts where:
 1. Elements in the array are positive (>= 0)
 2. Elements in the array are negative (<= 0)

'''

# For now let us see with the first part (Positive Part)


# BRUTEFORCE
'''
Its simple :
1. Calculate all the subarrays
2. Then I calculate the sum of each sub arrays and check if the sum is equal to K
3. If it is equal to K, then I continuously check the longest one and update it and finally return the answer
'''
def subArrayBruteforce(arr, k):
    subarray = []
    ans = 0
    curr = 0
    for i in range(len(arr)):
        subarray.append(arr[i])
        curr += arr[i]
        if arr[i] == k:
            ans = max(ans, len(subarray))
        # print(subarray, curr, ans)
        for j in range(i+1, len(arr)):
            subarray.append(arr[j])
            curr += arr[j]
            if curr == k:
                ans = max(ans, len(subarray))
            # print(subarray, curr, ans)
        
        curr = 0
        subarray = []
    return ans
            
print(subArrayBruteforce([1, 4, 1, 3, 1, 1, 2, 1, 2], 5))

# This is how you do it in the bruteforce way, The TC is O(N^2) and SC is O(1), Ofcourse you have to optimise this. And one more thing
# this will work for any elements in the array whether its positive or negative



# BETTER SOLUTION

'''
This is based on prefix sum, Once learn about prefix sum if you dont know about that. The approach follows these steps:
1. update prefix sum
2. check if p_sum == k
3. check if sum - k exists in the hash map
 -> If yes then there exists a sub array with sum k 
4. Add the prefix sum to the map

This is will work in all cases as well (Positive or negative elements)

'''

def subArrayPrefix(arr, k):
    dic = {}
    counter = 0
    ans = 0
    for i in range(len(arr)):
        counter += arr[i]
        if counter == k:
            ans = i+1
        else:
            if counter - k in dic:
                n = i - dic[counter-k]
                ans = max(ans, n)
        if counter not in dic:  # A check to avoid adding the latest same prefix sums if we have any zeroes
            dic[counter] = i
    return ans

print(subArrayPrefix([-1, -1, -1, -1, 1], 1))

# Its not bad at all, Its good but yes, its just that we are using space for dictinary, So
# TC - O(n), SC - O(n)


# OPTIMAL SOLUTION

# This approach is based on two pointer, More precisely on sliding window
'''
-------------------------------
Two Pointer / Sliding Window Approach
-------------------------------

Approach:
Use two pointers to represent the start and end of the subarray.
Maintain a running sum and adjust pointers based on comparison with the target sum (k).
Keep track of the maximum length of subarrays having sum equal to k.

-------------------------------
Explanation:
-------------------------------

1. Initialization:
   - sum : Keeps track of the running sum of the elements in the current subarray.
   - max : Stores the maximum length of subarrays with sum = k.
   - i, j : Represent the start and end pointers of the subarray.

2. While Loop (till j < n):
   - The loop continues until the end pointer j reaches the end of the array.
   - Inside the loop, there are three main cases:

   Case 1: sum == k  (Valid subarray found)
      - Calculate the current subarray length (len = j - i + 1).
      - Update max if len > max.
      - Move the end pointer (j) forward and add the next element to sum.

   Case 2: sum < k  (Need to increase the window size)
      - Increment end pointer (j) and add arr[j] to sum.

   Case 3: sum > k  (Need to shrink the window)
      - If i == j, it means a single element subarray itself exceeds k.
        Move both pointers forward and reset the running sum accordingly.
      - Otherwise, subtract arr[i] from sum and increment i (shrink from left).

3. Return Result:
   - Return max, which stores the length of the longest subarray having sum = k.

-------------------------------
Summary:
This approach uses two pointers (i, j) to dynamically maintain a window
whose sum is compared with k. Depending on whether the sum is less than,
equal to, or greater than k, the window is expanded or contracted.
The algorithm efficiently finds the longest subarray with sum = k.
-------------------------------
'''

def subArrayOptimal(arr, k):
    i,j = 0,0
    window = arr[0]
    ans = 0
    while j < len(arr):
        if window < k:
            j += 1
            if j < len(arr):
                window += arr[j]
        elif window > k:
            if i == j:   # This is for a case when both i and j point to the same element then both of them should move to the next one, not just i
                i += 1
                j += 1
                if i < len(arr):  
                    window = arr[i]
            else:
                window -= arr[i]
                i += 1
        else:
            ans = max(ans, j - i + 1)
            j += 1
            if j < len(arr):
                window += arr[j]
    return ans

# The TC is O(2*n) and SC is O(1)

# HEADSUP :
'''
This sliding window problem works only if there are positive or more precisely non negative elements or numbers, this will not work in the 
case of negatives because we are going with the assumption of moving the window to the right when the sum is less than the target, And this
will only happen if the numbers are positive, If the numbers are negative then moving the window to the right will inturn decrease the sum
and that contradicts out entire assumption and logic!!


For negatives :
There are only two methods -> Bruteforce, Better solution is the optimal solution
'''

print(subArrayOptimal([1, 4, 1, 3, 1, 1, 2, 1, 2], 3))

