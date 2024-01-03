# input = "Hello"
def recur_string(input):

    if len(input) <= 1:
        return input
    
    # input[0],input[-1] = input[-1], input[0]
    # return input[-1] + recur_string(input[:-1])
    #print( input[-1] + recur_string(input[:-1]))
    return recur_string(input[1:]) + input[0]

result = recur_string("Shahjalal")
print(result)