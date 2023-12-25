#Boolean
a = 10
b = 5
print(a>b)

if b>a:
    print("b is greater than a")
else:
    print("a is greater than b")

#Evaluate values and variables
print(bool("Hello"))
print(bool(a))

print(bool(["apple", "Cherry"]))

print(bool(False))
print(bool({}))

#Functions can return boolean
def myFun():
    return True

print(myFun())

if myFun():
    print("Yes")
else:
    print("No!")

x = 100
print(isinstance(x, float))
