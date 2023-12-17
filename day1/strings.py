#Multiline string
a = """Hello ,there is a man who havent noting and who 
have pure heart"""
print(type(a))

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