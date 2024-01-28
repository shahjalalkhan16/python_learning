# OOP Pillars
# Encapsulation

class Car:
    def __init__(self, color, brand):
        self.color = color # public variable
        self.__brand = brand # private variable

    # getter function
    def get_brand(self):
        return self.__brand 
    #private using __
        
    # setter function
    def set_brand(self, brand):
        self.__brand = brand

    

tousif_car = Car("red", "ferrari")

print(tousif_car.color)
print(tousif_car.get_brand())

tousif_car.__brand = "mercedes"
print("Direct update")
print(tousif_car.get_brand())

tousif_car.set_brand("mercedes")
print("after setter update")
print(tousif_car.get_brand())