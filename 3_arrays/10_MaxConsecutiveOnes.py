'''
Given an array of numbers we have to find the maximum number of consecutive ones in the array

'''

#Optimal Approach -> TC - O(n), SC - O(1)

def maxOnesOptimal(arr):
    curr = 1
    ans = 1
    for i in arr:
        if i == 1:
            curr += 1
            ans = max(curr, ans)
        else:
            curr = 0
    return ans
# So simple and so nice


# My approach -> TC - O(n), SC - O(1)
def maxOnes(arr):
    i = 0
    n = len(arr)
    while i<n and arr[i] == 0:
        i += 1
    j = i
    ans = 0
    temp = 0
    while j < n and i < n:
        if arr[j] == 1:
            temp += 1
            j += 1
            ans = max(temp, ans)
        else:
            i = j
            while i<n and arr[i] == 0:
                i += 1
            j = i
            temp = 0
    return ans

'''
Its definitely not better than the optimal method but its not too bad, That is why I am not removing it. The basic idea behind
this code is :

- Skip initial 0s
- Start counting when you find a 1
- Reset when you hit a 0
All of this is done using two pointers

'''

print(maxOnes([1,0,1,1,0,1,1,1,1,0]))