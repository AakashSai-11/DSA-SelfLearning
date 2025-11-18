def rec(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)-1
    ans = rec(arr[:length])
    last = [arr[-1]]
    return last + ans
    
print(rec([1,2,3,4]))