'''
This question is about finding out whether the array is sorted or not
'''

def checkSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            continue
        else:
            return False
        
    return True

print(checkSorted(list(map(int, input().split()))))

# TC - O(N) & SC - O(1)