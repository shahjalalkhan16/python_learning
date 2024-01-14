a = int(input("Enter a number:"))
b = int(input("Enter a number:"))

try:
    result = a + b

except Exception as e:
    print("Error occured!")
    print(e)


else:
    print("addition", result)

finally:
    print("Code finished!")
