dict = {
    "brand":"porche",
    "model": "911GT",
    "year": "1963"

}

print(dict.keys())

# for key in dict.keys():
#     print(f'key {key} - value {dict[key]}')

values = []
for key in dict.keys():
    values.append(dict[key])
#values = [dict[key] for key in dict.keys()]

# print(values)
    

numbers = [2, 3, 4, 5]

added_numbers =[]

for i in numbers:
    added_numbers.append(i + 3)

print(added_numbers)

added_numbers_online = [i+3 for i in numbers]

print(added_numbers_online)
