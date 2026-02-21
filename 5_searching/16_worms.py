# https://codeforces.com/contest/474/problem/B

def bin(target, arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low + 1


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))
s = []
counter = 0
for i in arr:
    counter += i
    s.append(counter)

for i in t:
    ans = bin(i, s)
    print(ans)
    