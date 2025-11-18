'''
This sorting method works by pushing maximum element to the right by swapping adjacent elements at each iteration

'''

def bubbleSort(arr):
    swapped = False
    n = len(arr)
    for i in range(n-1, 1, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            return arr
    return arr

print(bubbleSort([3,4,2,1,9,7]))

'''
Time complexity analysis :-

Bubble sort uses two nested loops. The outer loop runs from i = n-1 down to i = 1, effectively iterating through each element.
In the first iteration, the inner loop runs n-1 times.
In the second iteration, the inner loop runs n-2 times.
This pattern continues until the last iteration, where the inner loop runs only 1 time.

Time Complexity = 1 + 2 + 3 + ... + (n-1)
                = ((n-1) * (n-1+1))/2
                = (n * (n-1)) / 2
                = (n^2)/2 - n/2
                = O((n^2)/2 - n/2)
                = O(n^2)
                
 --> Worst and Average Case Time Complexity of Bubble sort is O(n^2), where n is the size of array

 --> Time Complexity will be O(n) for the best case.
 --> If the array is already sorted, the algorithm will make a single pass through the array to check if any swaps are needed. 
 In each pass, it will find the array is sorted, and the algorithm terminates early.

'''