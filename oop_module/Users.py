class User:
    """A basic program user"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.angry = False


    def describe_user(self):
        name = self.first_name + " " + self.last_name
        print(f"Fullname is {name}")

    def greet_user(self):
        print(f"hello {self.first_name}")

    def mood_kemon(self):
        if self.angry == True:
            print("valo na!")
        else:
            print("valo")
    
    def make_angry(self):
        self.angry = True
    
    def make_nice(self):
        self.angry =False

kafka = User("Kafka","Trumra")
kafka.describe_user()
print("Before mood:")
kafka.mood_kemon()

# directly updating an attribute
kafka.angry = True
print("After maramari ")
kafka.mood_kemon()

# updating through a function
kafka.make_angry()
print("After ragano")
kafka.mood_kemon()

kafka.make_nice()
print("Calmed down!")
kafka.mood_kemon()