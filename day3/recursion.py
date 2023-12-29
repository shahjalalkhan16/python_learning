 
#concepts
#base case
#recursive case

#recursive function

# a funtion has calls itself

# recursive case
def function():
    print("Hello")
    function()

#function()

# base case - return from the function

def recur_skel(a ):
    #base case
    if a <= 0:
        return
    
    #function
    print("got", a)

    #call the function itself
    recur_skel(a-10)

recur_skel(100)


#factorial calculation
# 5! = 5*4*3*2*1
# n! = n(n-1)...3 2 1

def  fac(n):
    #base case
    if n == 0:
        return 1
    
    #recursion
    return n*fac(n-1)
    

result = fac(5)

print(result)

def sum(n):
    if n == 0:
        return 0
    
    #recursive
    return n+ sum(n-1)

print(sum(5))


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


# palindrome using recursion
def is_palindrome(input):
    #base  case
    if len(input) <=1:
        return True


    #check if first and last character are the same
    if input[0] == input[-1]:
        return is_palindrome(input[1:-1])
    
    return False

print(is_palindrome("radar"))
