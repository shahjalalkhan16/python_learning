# map applies to iterables
# list, tuple


numbers = [1, 2, 3, 4, 5]

def do_square(x):
    return x*x


# squared = list(map(do_square, numbers)) # using define function
squared = list(map(lambda x: x * x , numbers)) # using lamda function


print(squared)

# def function_er_vitore_function(input_function):
#     print(input_function(5))

# function_er_vitore_function(do_square)

# convert lowercase string to upper case using map and lambda

words = ["hello", "world", "python"]

up = list(map(lambda x: x.upper(), words))

print(up)