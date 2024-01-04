numbers = [1, 2, 3, 4, 5]

words = ['hello', 'world', 'python']

# print(sorted(numbers, reverse=True))

# print(sorted(words, reverse=True))

students = [('Zbir', 1, 99), ('Rakib', 3, 100), ('Tumpa', 4, 70)]

#print(sorted(students, key=lambda pair: pair[2], reverse=True))

dict = {"tafka" : 10, "hemmingway": 5, "orwell": 3}
# print(dict['Kafka'])
# print(dict.keys())

keys = sorted(dict.keys())
print(keys)

empty_dict = {}
for key in keys:
    print(f"now adding key '{key}' values {dict[key]}")
    empty_dict[key] =dict[key]

print(empty_dict.items())