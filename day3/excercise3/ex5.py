#fibonacci using recursion
def fibo(n):
    #base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibo(n-1) + fibo(n -2)
    
    #check 


for i in range(5):
        print(fibo(i))