def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = 0
    right = len(arr)
    mid = left+right // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    ans = []
    i,j = 0,0
    while i<=len(left) and j<=len(right):
        if i==len(left):
            ans.extend(right[j:])
            break
        elif j == len(right):
            ans.extend(left[i:])
            break
        else:
            if left[i] < right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
    # print(ans)
    return ans


# print(merge_sort([5,4,8,1,2,10]))

'''
In place merge sorting :-

'''

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = 0
    n = right - left + 1
    new_arr = [0] * n
    
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            new_arr[k] = arr[i]
            i += 1
        else:
            new_arr[k] = arr[j]
            j += 1
        k += 1
    
    while i <= mid:
        new_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        new_arr[k] = arr[j]
        j += 1
        k += 1
    for c in range(n):
        arr[left + c] = new_arr[c]
    
        
    

def merge_sort_2(arr, left, right):
    if left == right:
        return
    
    mid = (left+right)//2
    print(arr[left:mid])
    print(arr[mid:right])
    
    merge_sort_2(arr, left, mid)
    merge_sort_2(arr, mid+1, right)
    merge(arr, left, mid, right)
    
    return

arr = [5,4,8,1,2,10]
merge_sort_2(arr, 0, len(arr) - 1)
print(arr)