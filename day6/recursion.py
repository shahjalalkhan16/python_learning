# calls itself

def recur_fibo(n):
    if n == 0:
       return 0
    
    elif n == 1:
        return 1
    
    #recursive case
    else:
       return recur_fibo(n-1) + recur_fibo(n-2)


print(recur_fibo(9))