def fibo(n):
    # base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# example usage
n = 10
for i in range(n):
    print(fibo(i))

