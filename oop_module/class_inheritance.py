# inheritance

class Animal:
    def __init__(self) :
        self.legs = 4
    
    def speak(self):
        print("Animal dake")
    

class Cow(Animal):
    # def __init__(self):
    # self.legs = 4

    def speak(self):
        print("Homba")
    
    def jabor_kata(self):
        print("eating")

class Goat(Animal):
    def __init__(self):
        self.legs = 3
    
    def beshi_dake(self):
        print("baa baaaa")


goru = Cow()
chagol = Goat()

print(goru.legs)
print(chagol.legs)
goru.speak()
chagol.speak()
