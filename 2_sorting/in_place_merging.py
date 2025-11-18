'''
def merge(arr1, arr2, n, m):
    i = 0
    j = 0
    while i<n and j<m:
        if arr1[i] < arr2[j]:
            i += 1
            continue
        else:
            arr1[i],arr2[j] = arr2[j],arr1[i]
            i += 1
            k = j
            while k<m-1 and arr2[k] > arr2[k+1]:
                arr2[k], arr2[k+1] = arr2[k+1], arr2[k]
                k += 1
    return arr1,arr2

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
n = len(arr1)
m = len(arr2)

print(merge(arr1, arr2, n, m))

The above method works as well, I mean ofcourse why not, I did it on my own but the thing is the time complexity is O(m * n), which is
not very impressive to be honest. Well there are two optimal and better approaches which I will be writing below :

METHOD 1 :-

This method has a very simple approach, you somehow try to bring all the necessary elements of two arrays and then finally sort it.
It works like this:
- You will have a left pointer towards the end of first array
- You will have a right pointer towards the beginning of the second array
- You compare and if you have less element in the second one you swap it, until unless you dont have any less elements in the second array
- Think about it, Now you basically have all the less elements in the first array and the higher elements in the second array
- Now you just need to sort both of them and yayyy, we get out required answer

'''

'''
def merge1(arr1, arr2):
    i = len(arr1) - 1
    j = 0
    while arr1[i] > arr2[j]:
        arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1
    arr1.sort()
    arr2.sort()
    
arr1, arr2 = [-5, -2, 4, 5],[-3, 1, 8]
merge1(arr1, arr2)
print(arr1, arr2)

Its an interesting method, the time complexity is O(min(m,n)) + O(mlogm) + O(nlogn)

'''

'''
METHOD 2 :-

This is method is known as the gap method and it is taken from the shell sort, This basically involves taking a certain amount of gap
which is calculated by summing the both array lengths and then dividing it by 2 and finally taking its ceil value

- Now that we have calculated the gap value, we start by taking two pointers
- First one is ofcourse at the beginning of the first list and the second one is the gap distance away from the first pointer
- Remember that in this method, you basically consider both arrays as one big array and proceed
- If the order of two elements in the both pointers is not correct swap them, order means that the left element should be always smaller
than the right element
- When the right pointer is exhausted, update the gap value by dividing it with 2 and then again taking its ceil.
- Continue this process till we get the gap as 1.
- When we do the final process for gap = 1, we get the both arrays as automatically sorted

'''

'''
def nextGap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)

def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    gap = nextGap(m + n)

    while gap > 0:
        i = 0
        j = gap

        while j < (m + n):
            # Case 1: both in arr1
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            # Case 2: i in arr1, j in arr2
            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

            # Case 3: both in arr2
            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        gap = nextGap(gap)

    return arr1, arr2


arr1 = [-5, -2, 4, 5]
arr2 = [-3, 1, 8]
merged = merge(arr1, arr2)
print(merged)

# print(arr1, arr2)

Its a very great approach, I didnt even know about this shit earlier, well that's that
The time complexity of this shit is as follows :

- The gap starts at ceil((n + m) / 2) and reduces by half in each iteration until it reaches 1, resulting in O(log(n + m)) iterations.
- In each iteration, we compare and possibly swap elements across both arrays. This takes O(n + m) operations per iteration, 
  since we are traversing both arrays linearly.
- Hence, the overall time complexity is the product of the number of iterations and the operations per iteration: O((n + m) log(n + m)).

'''