#Multiline string
a = """Hello ,there is a man who havent noting and who 
have pure heart"""
print(type(a))

#slicing
print(a[6:10])
print(a[-10:-3])

#Check string
cs = "is" in a
print(type(cs))

#if not
if "mans" not in a:
    print("not mans")

#Slice
b='Hii man'
print(b[:5])
print(b[2:])

x ="  HeLlo, friEnds "
print(x.upper())
print(x.lower())
print(x.strip())
print(x.replace("H","J"))
print(x.split(","))
X = "hnkj vfbdddddd"
print(X.capitalize())

#concate
p = "Hello"
q = "There"
r = p+q
print(r)
#string format
age = 23
txt = "This is Shahjalal Khan {}" 
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#Escape character
esc = "This is me \"who\" havent nothing"
print(esc)



