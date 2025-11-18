def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(5))


'''
The time complexity of this is O(2^N), This refers to exponential time complexity
The exciting derivation of this is :-

Step-by-Step Derivation

1. Recurrence relation
T(n) = T(n-1) + T(n-2) + C

2. Replace T(n-2) by T(n-1) (upper bound) -> I mean for large cases of n(Some 1000000), both n-1 and n-2 are approximately same so
consider both of them as n-1 itself

T(n) = T(n-1) + T(n-1) + C

T(n) = 2T(n-1) + C => (X)

3. Expand T(n-1) ->  Basically Substituting n-1 in the above equation X
T(n-1) = 2T(n-2) + C  => (Y)

So, Now Substitute Y in X:

T(n) = 2(2T(n-2) + C) + C

T(n) = 2^2 T(n-2) + 3C  => (Z)

4. Expand T(n-2) -> Basically Substituting n-2 in the above equation X
T(n-2) = 2T(n-3) + C  => (F)

So, Now Substitute F in Z:

T(n) = 2^2 (2T(n-3) + C) + 3C

T(n) = 2^3 T(n-3) + 7C  => (D)

5. General form (after k steps)
T(n) = 2^k T(n-k) + (2^k - 1)C 

--- I mean understand it like this, for first step we got 2, for second step when we substitute for n-1 we get 2^2 and then when we
substitute n-2 we get 2^3, Similary the coefficients for constants respectively are 1 at the start, 3 and then 7 which are in the form of
2^k - 1 ---

6. Substitute k = n

T(n) = 2^n T(n-n) + (2^n - 1)C

T(n) = 2^n T(0) + (2^n - 1)C

7. Simplify
Let T(0) = C1

T(n) = 2^n * C1 + (2^n - 1) * C

T(n) = 2^n * C1 + (2^n * C) - C

8. Taking 2*n common
T(n) = (C1 + C) * 2^n - C

Let C1 + C be C2

T(n) = C2 * 2^n - C

Final Result:
T(n) = O(2^n)


This is what I call absolute Magic!!!

'''

