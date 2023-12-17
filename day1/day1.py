print('Welcome to new programming language!')

#Arithmetic operation
sum = 2+4
print('Addition of two numbers: ',sum)
subtract = 6-2
print('Subtract of two numbers:',subtract)
mul = 2*3
print('Multipication of two numbers:', mul)
divisor = 11/3
print('Divisor of 9 and 3 : ', divisor)
re = 5%2
print('Remender is:', re)

#Mathematical operation

#p = 3**2
p = pow(4,3)
print('Power is: ', p)

import math
sqt = math.sqrt(7)
print('Square root: ',sqt)

# casting
x ='3'
print(4+int(x))

print(type(x))

#multi value 
a,b,c = 'I', 'am', 'Shahjalal'
print(a,b,c)

#Unpack collection

fruits =['apple', 'orange', 'banana']
p,q,r = fruits
print(p)
 
xy = 'Global Variable'

def my_fun():
 print(xy)

my_fun()