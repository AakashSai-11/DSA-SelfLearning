def recursive_print(m,n):
    if n==m or n==0:
        return
    print(n)
    recursive_print(m,n+1)
    print(n)
    
recursive_print(6,1)

#This was a simple method to print 1 to n and then n to 1 

