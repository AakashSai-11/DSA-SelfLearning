

def merge(arr, left, mid, right):
    ans = 0
    i = left
    j = mid + 1
    k = 0
    n = right - left + 1
    new_arr = [0] * n
    while i<=mid and j<=right:
        if arr[i] <= arr[j]:
            new_arr[k] = arr[i]
            i+=1
        else:
            new_arr[k] = arr[j]
            ans += mid-i+1
            j+=1
        k += 1
    while i<=mid:
        new_arr[k] = arr[i]
        i+=1
        k+=1
    while j<=right:
        new_arr[k] = arr[j]
        j+=1
        k+=1
    for c in range(n):
        arr[left+c] = new_arr[c]
    return ans

def msort(arr, left, right):
    count = 0
    if left == right:
        return 0
    mid = (left + right) // 2
    count += msort(arr, left, mid)
    count += msort(arr, mid+1, right)
    count += merge(arr, left, mid, right)
    return count
    
    
arr = list(map(int, input().split()))
n = len(arr)
print(msort(arr, 0, n-1))


