'''
Given two sorted arrays, We have to return a new array which will have the elements the same as the union of those two arrays

Example -

a = [3, 3, 4, 5, 6, 6]
b = [4, 5, 6, 7, 8, 8]

The resultant array should be the union of these two that is the final answer is [3, 4, 5, 6, 7, 8]
=> Basically all the elements of a and b but no repetition

-> Bruteforce :-
1. Simply create a set and then add all those elements
2. Then copy those elements into a list and then finally return a sorted list
3. TC - O(m+n)log(m+n), SC - O(m+n)


-> Optimal Solution :-
1.Use two pointers to traverse the sorted arrays arr1 and arr2 simultaneously.
2.Compare the current elements from both arrays and add the smaller (or equal) element to the answer container if it is not a duplicate.
3.After completing the simultaneous traversal, if any elements remain in arr1 or arr2, 
  process them individually—adding each unique element to the answer container.
4.The result is a merged, sorted container that contains only unique elements from both arr1 and arr2.
5. TC - O(m+n) , SC - O(m+n)

'''

def union_of_two_sorted_arrays(a,b):
    ans = [-1]
    m,n = len(a),len(b)
    i,j = 0,0
    while i<m and j<n:
        if a[i] < b[j]:
            if ans[-1] != a[i]:
                ans.append(a[i])
            i += 1
        else:
            if ans[-1] != b[j]:
                ans.append(b[j])
            j += 1
    while i < m:
        if ans[-1] != a[i]:
            ans.append(a[i])
        i += 1
    while j < n:
        if ans[-1] != b[j]:
            ans.append(b[j])
        j += 1
    ans = ans[1:]
    return ans

print(union_of_two_sorted_arrays([3,3,4,5,6,7],[4,5,6,7,8,8]))