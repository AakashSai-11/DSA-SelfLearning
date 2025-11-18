'''
Given two sorted arrays we have to calculate the intersection of those two arrays, Basically we have to return the new array which
only contains the common elements of those two arrays that to in a sorted order

So actually there is one more thing you should look into, its that this problem actually wants the output in a paired format kind of 
thing

so if we have the input arrays like this
a -> [2,3,3,3,4,5]
b -> [3,3,4,4]

The output we should get is [3,3,4]
That is because there are two 3s common in both the arrays, that is why we have to get two 3s there

Bruteforce way of solving is taking another array to manage the second array and keeping track of whether the number is paired or not.

'''

# TC -> O(m*n), SC -> O(2k), at a worst case scenario where k is the min(a,b)
def bruteforce_intersection(a,b):
    ans = []
    temp = [0] * (len(b))
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and temp[j] == 0:
                ans.append(a[i])
                temp[j] = 1
                break
            if a[i] < b[j]:
                break





# My approach -> TC - O(m+n), SC - O(min(a,b)) for storing the ans
# This is the optimal approach it self, So yeah this is how you do it
def intersection(a,b):
    arr = []
    m,n = 0,0
    while m<len(a) and n<len(b):
        if a[m] == b[n]:
            arr.append(a[m])
            m += 1
            n += 1
        elif a[m] < b[n]:
            m += 1
        else:
            n += 1
    return arr



# My approach -> TC - O(m+n), SC - O(k)
'''
I made it a bit more interesting, here we should only get the common numbers once and not in a paired format kind of thing
'''
def intersection2(a,b):
    arr = ['h']
    m,n = 0,0
    while m<len(a) and n<len(b):
        if a[m] == b[n] and arr[-1] != a[m]:
            arr.append(a[m])
            while m < len(b) and a[m] == arr[-1]:
                m += 1
            while n<len(b) and b[n] == arr[-1]:
                n += 1
        elif a[m] < b[n]:
            while m+1<len(a) and a[m] == a[m+1]:
                m += 1
            m += 1
        else:
            while n+1<len(b) and b[n] == b[n+1]:
                n += 1
            n += 1
    
    return arr[1:]

print(intersection2(
    [1,2,3,4,5,6,7,7,7,7],
    [2,3,4,5,7,9,9]
))
         
            
    