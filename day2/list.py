myList = ["apple", "banana","cherry"]
print(myList)

print(myList[1])
#length
print(len(myList))

#diff data in a list
myList1 = ["Hello", "There", 5, False]
print(myList1)

print(type(myList1))

#list() constructor when creating a new list
theList = list(("mango", "pineaple"))
print(theList)

#indexing
print(theList[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[3:5])
#check if item exits
if "apple" in thislist:
    print("Yes, apple is in the list")

#change item vale
theList[1] = "jame"
print(theList)
#change the range
thislist[1:3] = ["pipeapple", "watermelon"]
print(thislist)

#insert item
theList.insert(1,"dragon")
print(theList)
#append item in the last position
theList.append("lichi")
print(theList)
#To append elements from another list to the current list
theList.extend(thislist)
print(theList)

#add any iterable
l = ['a','b']
t = (1,2)
l.extend(t)
print(l)