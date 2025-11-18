'''
You are given a sorted integer array. Your task is to return a new array that contains the squares of each element in array, sorted in
non decresing order.

Ex - 
Given -> [-5, -1, 0, 3, 6]
Output -> [0, 1, 9, 25, 36]

Optimal Approach -

Initialize the Result Array:
- Create a result array of the same size as the input array to store the sorted squares.

Use Two Pointers:
- Start with two pointers: left at the beginning of the array, and right at the end.
- Compare the absolute values of the elements at these two pointers.

Build the Sorted Squares:
- If the element at the left pointer is larger when squared, place its square at the current position in the result array.
- Otherwise, square the element at the right pointer and place it in the result array.
- Move the corresponding pointer (left or right) inward after placing the square.

Fill the Result Array:
- Continue this process until the entire result array is filled with squared elements in non-decreasing order.

Final Output:
- After all elements are squared and placed in the result array, return the sorted result.

'''

def squares_order_array(arr):
    n = len(arr)
    ans = [-1] * (n)
    k = n-1
    i,j = 0,n-1
    while i <= j:
        x = arr[i] ** 2
        y = arr[j] ** 2
        if x > y:
            ans[k] = x
            i += 1
        else:
            ans[k] = y
            j -= 1
        k -= 1
    return ans

print(squares_order_array([-5, -1, 0, 3, 6]))