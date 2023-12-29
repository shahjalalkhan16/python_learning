# data = [2,5,4,7,1]
# print(sorted(data))

# def inc_by_ten(x):
#     return x+10

# print(inc_by_ten(30))

equivalent = lambda x: x+10

people = [("my", 5), ("friends",2),('friends',3)]

people.sort(key = lambda pair: pair[1])
#print(people)

students = [("kafika",1,83),("orwell",2,70),("hemingway",3,95)]
students.sort(key= lambda pair: pair[2], reverse=True)
#print(students)

# def without_lambda_sort(pair):
#     #pair: (string,int,int)
#     #sort based on goodness
#     return pair[2]

# people.sort(key=without_lambda_sort)

# print(people)