def bin(target, arr):
    low = 0
    high = len(arr)-1
    
    while low < high:
        mid = low + (high-low)//2
        
        if arr[mid] < target:
            low = mid
        else:
            high = mid - 1
    
    return high
  
n, t = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
for i in range(t):
    inp = int(input())
    ans = bin(inp, arr)
    print(len(arr)- ans - 1)