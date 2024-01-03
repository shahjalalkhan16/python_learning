# while condition:
#     statement


# count = 1
# i = 0
# while count <= 5:
#     print(count)
#     count = count + i
#     i = i+ 1
# print("Done")

# word = ""
# sentence = " "
# while word != "stop":
#     word = input("Enter a word (Please type 'stop' to end): ")
#     print("You entered: ", word)
#     sentence = sentence + " "+ word
# print("That was fun!")
# print(sentence)

# count = 1

# while count <=3:
#     print(count)
#     count += 1
# else:
#     print("Here", count)
#     print("loop ended")
#     count -= 1

# print(count)

# count = 1

# while count <=5:
#     print(count)

# count = 1 
# print (count <= 5) #return boolean 
#while True:
    #print("This will print forever ")


# i = 0
# while i < 5:
#     j = 0
#     # print(f"outside: i: {i} and j: {j}")
#     while j < 5:
#         print(f"here: i: {i} and j: {j}")
#         j += 1
#     i += 1

building = [
    ["G1", "G2", "G3","G4"], 
    ["A1", "A2", "A3","A4"],
    ["B1","B2","B3", "B4"]

] #2D matrix - 3 x 4

# row  = 3
# column = 4
floors = 3
apartments = 4

# for i in range(floors):
#     print("now in floor: ", i)
#     for j in range(apartments):
#         #print(f"knocking on apartment {j}")
#         print(f"knocking on apartment: ", building[i][j])

for floor in building:
    print("now", floor)
    for apartment in floor:
        print("Knocking on: ", apartment)

#floor1  = ["G1", "G2", "G3"]
