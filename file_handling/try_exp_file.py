fileName = "mytext.txt"


try:
    with open(fileName, "r") as file:
       # file.write("Hello try except block!")
        print(file.read())

except Exception as e:
    print("ERROR!")
    print(e)

finally:
    print("Programe done!")