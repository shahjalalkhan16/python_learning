# clasnames start with  a capital letter in python

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # # python does not support constructor overloading
    # def __init__(self):
    #     pass


    def eat(self):
        print(f"Now {self.name} is eating!")
    
    def sleep(self):
        print(f"Now {self.name} is sleeping")


my_cat = Cat("Puffy", "3")

print("Name of my cat ", my_cat.name)
my_cat.eat()
my_cat.sleep()

# my_puffy = Cat()
# my_puffy.eat()