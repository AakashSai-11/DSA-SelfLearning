'''
Given an array which has number upto given range and we have to find one missing number that will be in the range

'''

# Bruteforce
def missingNumber(arr, r):
    for i in range(1,r+1):
        if i not in arr:
            return i
# This is costly process as the loop runs for every check, TC -> O(n*2) for worst case and SC -> O(1)


#Better solution

def missingNumber2(arr, r):
    temp = [0] * (r+1)
    for i in arr:
        temp[i] = 1
    for i in range(1,r+1):
        if temp[i] == 0:
            return i
# This solution uses one more temporary array to mark the absence of the required number, TC - O(2*n), SC - O(n)



# Optimal
def missingNumberOptimal(arr, r):
    s = sum(arr)
    actual = r * (r+1) // 2
    return actual - s

# very optimal, It uses sum of n natural numbers application above and its a linear time complex solution
'''
-> EDGE CASE ALERT :
It seems that there is an edge case here, For suppose we have a range of 10^6 then we have to store something equal to 10^12 which ideally
is not possible for integer data type as the limit is ~10^9 in c++ or maybe java too, Idk about java but its true for c++ 
and for that reasons you have to use long long to avoid this error for larger inputs.
- That's why you have to use python (Being weirdly proud of myself lol)!! (JK I know nothing can beat c++ though)

'''

# Optimal method using XOR, Unique and yet one more optimal method of the question
'''
------------------------------------------------------------
Optimal Solution - 2 : Using XOR Bitwise Operator
------------------------------------------------------------

-------------------------
AND Bitwise Operator (&)
-------------------------
When both operands are 1 → result is 1
When operands are different (0 or 1) → result is 0

Example:
    a = 1011
    b = 0101
    res = 0001

-------------------------
OR Bitwise Operator (|)
-------------------------
When both operands are 0 → result is 0
When operands are different (0 or 1) → result is 1

Example:
    a = 1010
    b = 0110
    res = 1110

-------------------------
XOR Bitwise Operator (^)
-------------------------
When operands are the same (0 or 1) → result is 0
When operands are different (0 or 1) → result is 1

Example:
    a = 1010
    b = 1100
    res = 0110

-------------------------
More XOR Examples
-------------------------
A = 1011
A ^ A = 1011 ^ 1011 = 0000
A ^ 0 = 1011 ^ 0000 = 1011  → (same as A)

a = 1011, b = 0100, c = 1110
a ^ b ^ c = 1011 ^ 0100 ^ 1110
           = (1011 ^ 0100) ^ 1110
           = 1111 ^ 1110
           = 0001

------------------------------------------------------------
Approach to Find Missing Number in an Array (Using XOR)
------------------------------------------------------------
1. Initialize two XOR variables (xor1 and xor2) to 0.
2. Iterate through the array:
      - XOR each array element with xor1
      - XOR each index (i + 1) with xor2
3. Return (xor1 ^ xor2 ^ n)
   → This gives the missing number.

-------------------------
Pseudo Code
-------------------------
missingnumber(arr, n):
    xor1 = 0
    xor2 = 0
    for i from 0 to n - 2:
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ (i + 1)
    return (xor1 ^ xor2) ^ n

-------------------------
Explanation
-------------------------
Step 1: Initialize Variables
    xor1, xor2 = 0
    → xor1 stores XOR of all array elements
    → xor2 stores XOR of all numbers from 1 to n

Step 2: Calculate XORs
    for i in range(0, n - 1):
        xor1 ^= arr[i]
        xor2 ^= (i + 1)

Step 3: Find Missing Number
    missing_number = (xor1 ^ xor2) ^ n
    return missing_number

    The XOR operation cancels out all matching numbers
    and leaves only the missing number.
------------------------------------------------------------
'''

def missingNumberXOR(arr, n):
    xor1 = 0
    xor2 = 0
    for i in range(n - 1):
        xor1 = xor1 ^ arr[i]
        xor2 = xor2 ^ (i + 1)
    return xor1 ^ xor2 ^ n

# Its a very unique way and very interesting one as well, I couldnt accept it but this feeling is not new in dsa, Well for more clarity
# Refer this -> https://chatgpt.com/share/68ffd593-4ca0-800a-a4e1-1ed82af164d3

print(missingNumberOptimal([5,3,1,6,2],6))
