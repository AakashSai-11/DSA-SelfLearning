'''
Algorithm for Insertion Sort :-

1. Insert last element of the range to their correct position
2. Start the range with intial 2 elements
3. Increase range by 1

'''

def inertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while arr[j] < arr[j-1] and j>=1:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    
    return arr

print(inertionSort([100,40,20,70,30]))
                

'''
Time Complexity Analysis :-

For i going from 1 to n-1:
When i = 1, we perform 1 operation.
When i = 2, we perform 2 operations.
When i = n-1, we perform n-1 operations.

-> Time Complexity = 1 + 2 + 3 + ... + (n-1)
                = ((n-1) * (n-1+1))/2
                = (n * (n-1)) / 2
                = (n^2)/2 - n/2
                = O((n^2)/2 - n/2)
                = O(n^2)

-> Worst and Average Case Time Complexity of Insertion sort is O(n^2), where n is the size of array

Best Case Time Complexity: 
When the given array is already sorted
-> Time Complexity will be O(n)

i = 0: The first element, 5, is already in its correct position because there are no smaller elements before it
i = 1: The second element, 10, is greater than the element before it (5). So, we leave it in place
i = 2: The third element, 15, is greater than the element before it (10). So, we leave it in place
i = 3: The fourth element, 30, is greater than the element before it (15). So, we leave it in place
i = 4: The fifth element, 40, is greater than the element before it (30). So, we leave it in place

'''