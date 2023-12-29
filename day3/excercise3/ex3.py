students = [("kafika",1,83),("orwell",2,70),("hemingway",3,95)]
students.sort(key= lambda pair: pair[2], reverse=True)
print(students)