'''
Algorithm :

- Select a pivot element which is generally the arr[low]
- Place the pivot element at its correct position as in sorted array and create partition along pivot
- We repeat this process for all the partitions through recursion until the array is sorted.


'''

def partition(arr, low, high):
    pivot = arr[low]
    i = low+1
    j = high
    while i <= j:
        if arr[i] > pivot and arr[j]<=pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] < pivot:
            i += 1
        elif arr[j] > pivot:
            j -= 1

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low<high:
        j = partition(arr, low, high)
        quick_sort(arr, low, j-1)
        quick_sort(arr, j+1, high)
    
    return

arr = [11, 8, 5, 13, 12, 16, 9]
print(partition(arr, 0, len(arr)-1))
quick_sort(arr, 0, len(arr)-1)
print(arr)
    

'''
Time Complexity:

Best Case: O(n*log(n))
Average Case: O(n*log(n))
Worst Case: O(n^2)

Space Complexity:

For Additional space:
Worst Case: O(1)

For Stack Space:
Best Case: O(log(n))
Worst Case: O(n)

'''