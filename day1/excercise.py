name = "Hello there"
print(len(name))

#type 
print(type(name))

b1 = 30
b2 = 25

#function
def ages():
 if b1 >b2:
    print("first one is ender")
 elif b2  == b1:
        print("Both are same")
 else:
      print("Second one is eder")

ages()

#index of list
numbers=[3, 5, 1, 9, 7, 2, 8 ]
print(numbers.index(7))

# sorting the list in ascending order
numbers.sort()
print(numbers)

#isLandscape function

def isLandscape(width, height):
    if width> height:
        print("Landscape")
    else:
         print("Portrait")


isLandscape(400, 300)

def fizzBuzz(num) :
    if num % 3 ==0 and num % 5 ==0:
        print("FizzBuzz")
    elif num % 3 == 0 :
       print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print("Not a fizz-buzz number")

fizzBuzz(45)

#Gussing Game
def gussGame():
    tar = 5
    user = int(input("Enter your guess number: "))

    if user < tar:
        print("Your guess is almost there")
    elif user>tar:
        print("your guess is higher")
    else:
        print("Your guess is correct!")

gussGame()

#check if 6 in list
num = [4, 8, 7, 4, 3, 2, 1, 9]

if 6 in num:
    print("6 is here")
else:
    print("6 is not here")
    
        

