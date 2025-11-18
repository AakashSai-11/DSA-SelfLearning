'''
We will be looking at selection sort in this

Algorithm :

-> Select the min in the array
-> Swap the min with the first element
-> Reduce the range/ move the range to the right


'''

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]    
    
arr = list(map(int, input().split()))
selectionSort(arr)
print(arr)

'''
Time Complexity = n + (n-1) + (n-2) + ...... + 2
                = n + (n-1) + (n-2) + ...... + 2 + 1  ----> Adding 1 for approximation (which doesn't affect the time complexity)
                = n(n + 1)/2
                = ((n^2)/2) + (n/2) ----> Ignoring constants and lower powers
                = O(n^2)

'''