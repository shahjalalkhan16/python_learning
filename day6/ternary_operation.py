
#ternary operation
# x = int(input('Enter a number: '))

# if x < 5:
#     print('smaller than 5')

a  = int(input('Enter a number a: '))
b  = int(input('Enter a number b: '))
c  = int(input('Enter a number c: '))



# if a <b:
#     min = a

# min = a if a < b else b
# print('minimum is ', min)

# print('Both equal' if a == b else 'they are not equal')

# tuple

# we need to return the smallest number from (x,y)
# print((b, a) [a < b]) # index hisebe used for  b

min = a if a < b and a < c else b  if b < c  else c
print(min)