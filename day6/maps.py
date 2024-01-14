#map(function, iterable)

input_list =[1, 2, 3, 4]

def fun(x):
    return x*x

output_list = map(fun, input_list)

# print(tuple(output_list))

temperature1 = [0, 30, 50]

def convert_c2f(c):
    return (c*9/5) + 32

print(list(map(convert_c2f, temperature1)))


temperature = []

for temp in temperature1:
    tf = convert_c2f(temp)
    temperature.append(tf)

print(list(temperature))