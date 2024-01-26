class Resturant:
    """"Resturant class"""

    def __init__(self, name, cousine = None):
        self.name = name
        self.cousine = cousine

    def describe_resturant(self):
        print(f"This is a  resturant which name is {self.name}")

    def status(self, time):
        time = time.split(":")
        h = int(time[0])
        m = int(time[1])
        meridian = time[-1]
        if (h >= 9 and meridian == "AM") or (h <= 11 or m <= 30 and meridian == "PM"):
            print(f"{self.name} is now open!")
                # print(time)
        else:
            print(f"{self.name} is now closed!")


my_resturant = Resturant("The Bangala", "Bangla")

my_resturant.describe_resturant()
my_resturant.status("11:45:PM")

my_chines_res = Resturant("ChinesResturant", "Chines")

# my_chines_res.status()
