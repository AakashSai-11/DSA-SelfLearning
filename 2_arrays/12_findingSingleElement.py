'''
So this problem is about finding the single element in the array where basically all other elements appear twice and we have to find that
one element that appears only once

- BRUTEFORCE:
Ofcourse the bruteforce way of doing it is simply iterating the entire array for every element and finding the count of that element 
and then returning the count if it equals 1, I am not going to write that as its very much doable on own
  => TC - O(N^2), SC - O(1)

- BETTER SOLUTION:
So I think its kind of direct and easy as well, this method is simple, We use a hashmap (dictionary in python) and store the 
frequency count of all the elements of the array and then finally iterate through that dictionary and finally return the
key whose value is 1
  => TC - O(N), SC - O(N/2)

'''

# Optimal way

def singleElement(arr):
    ans = 0
    for i in arr:
        ans = ans ^ i
    
    return ans

print(singleElement([3,4,5,3,4,5,9]))

'''
This optimal way is based on XOR, We have looked into this in previous method as well where if we xor the same element we get 0,
So here as we can see that all the elements appear twice so we can say that each of those elements get cancelled during xor and only one
element remains which appears only once and in this way we can find our answer
 => TC - O(n), SC - O(1)

'''

#############


# Variation of the same question :
'''
You are given an integer array nums containing n + 1 integers, where each integer is in the range [1,n]. There is exactly one integer that
is repeated twice in the array. Your task is to find and return this repeated number

Example:
nums = [1, 2, 3, 2, 4]
Output = 2

nums = [4, 1, 3, 3, 2]
Output = 3

'''

def repeatingNumber(arr):
    n = len(arr) - 1
    s = sum(arr)
    actual = n * (n+1) // 2
    return s - actual
  

# There is actually an extended and deadly version of both of the above problems, Basically the mixed question of both of them, I will 
# try to cover it in the next file/Module, Atleast I will leave it open so that I can write it again later and dont forget it
