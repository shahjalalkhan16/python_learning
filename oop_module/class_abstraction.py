# abstraction class
class Car:
    def __init__(self) -> None:
        pass

    def start(self):
        self.check_engine()

    def check_engine():
        # complex code happening here
        print("Engine is good")


# Polymorphism

class Bird:
    def speak(self):
        print("Tweet")


class Dog:
    def speak(self):
        print("Bark")

bird_obj = Bird()
dog_obj = Dog()

animals = [bird_obj, dog_obj]

for animal in animals:
    animal.speak()