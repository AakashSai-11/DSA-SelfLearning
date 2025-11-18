def summ(i):
    if i==0:
        return 0
    return i + summ(i-1)

print(summ(5))


# Factorial :-

def fact(i):
    if i == 1:
        return 1
    return fact(i-1)*i

print(fact(5))