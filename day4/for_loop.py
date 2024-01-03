#syntax

# for i in range(1,5):
#     print(i)


# fruits = ["apple", "banana", "cherry"]
# # for fruit in fruits:
# #     print(fruit)
# another = []
# for fruit in fruits:
#     fruit = fruit.upper()
#     another.append(fruit)

# print("Upper: ", another)
# print("Fruits: ", fruits)

#reverse string
input = "Nongodev"
reversed = ""

# for letter in input:
#     reversed = reversed + letter

# print(reversed)

# for i in range(input[len(input)-1], input[1]):
#     print(i)
#     reversed = reversed +i

# print(reversed)

for i in range(len(input)-1, 0, -1):
    #print(input[i])
    reversed = reversed + input[i]

print(reversed)
    
# for i in range(2,30,3):
#     print(i)
# else:
#     print("finally finished")