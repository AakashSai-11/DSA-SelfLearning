'''
Return the index of the element if it is present in the array, Done in two ways, we are now using linear search

'''

def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

print(linear_search([1,24,5,3,7,8], 8))