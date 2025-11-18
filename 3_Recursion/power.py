def power(a,b):
    if b==0:
        return 1
    half = power(a,b//2)
    
    if b%2 == 0:
        return half * half
    else:
        return half * half * a

print(power(2,10))

# the time complexity here is o(log(b))
'''
The concept here is dividing the calculation based on odd and even powers, if the power is even, you divide the power into half and return
the square of the number and if it is odd, you reduce it, divide it and then you multiply the remaining 'a' and then square it 

'''