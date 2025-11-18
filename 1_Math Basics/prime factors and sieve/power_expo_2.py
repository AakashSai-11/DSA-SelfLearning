'''

We are going to learn about exponents and power calculation, given two number x and m we have to give the x power m value,
for example x = 2, and m = 5, the value that should be returned is 32. In c++, or in any language we have tools for that but this is
the internal logic :

APPROACH 1 ->  The naive approach which everyone can think of is just taking product value as 1 and then repeated multiplying x to that 
product m times to get the x pow m value, This has the time complexity of O(M) which obviously is not the optimal solution

APPROACH 2 -> It is a nice method, I will write down the code first and then the explanation

    x = 2   # base value (you can change this)
    m = 10  # exponent value (you can change this)
    ans = 1  # initialize result to 1

    while m != 0:
        if m % 2 == 0:
            # If m is even, divide m by 2 and square x
            m = m / 2
            x = x * x
        else:
            # If m is odd, multiply ans by x and reduce m by 1
            ans *= x
            m -= 1

    print(ans)
    ```

    ---

    Explanation:

    * Binary Exponentiation reduces the number of multiplications.
    * Instead of multiplying x m times (which takes O(m)), we:

    * Square x when m is even (x², x⁴, x⁸, etc.).
    * Multiply ans with x when m is odd.
    * This makes the loop run in log₂(m) steps.

    The time complexity is O(log(n)) which is very good!
    => The point to remember here is that if m is negative i.e, the power is negative we simply repeat the same process and then 
    finally divide 1 by answer. 

'''