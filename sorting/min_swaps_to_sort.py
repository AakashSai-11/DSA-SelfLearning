'''
The idea of the problem is that We want to find minimum number of swaps to sort an array.
'''
def minSwaps(arr):
    s = sorted(arr)
    ans = 0
    from collections import defaultdict
    k = defaultdict(int)
    for i in range(len(arr)):
        k[arr[i]] = i
    i = 0
    while i < len(arr):
        if s[i] != arr[i]:
            m = k[s[i]]
            arr[i], arr[m] = arr[m], arr[i]
            k[arr[i]] = i
            k[arr[m]] = m
            ans += 1
        i += 1
        
    
    return ans

print(minSwaps([43, 24, 41, 26, 35, 40, 15, 36, 18, 31]))
    
    