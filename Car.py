class Car:
    # Properties
    color = ""
    brand = ""
    number_of_wheel = 4
    number_or_seats = 4
    maxspeed = 0

    # Constructor
    def __init__(self, color, brand, number_of_wheel, number_or_seats, maxspeed):
        self.color = color
        self.brand = brand
        self.number_of_wheel = number_of_wheel
        self.number_or_seats = number_or_seats
        self.maxspeed = maxspeed

    # Create Method set color
    def setcolor(self, x):
        self.color = x

    def setbrand(self, x):
        self.brand = x

    def setmaxspeed(self, x):

        self.maxspeed = x

    def printdata(self):
        print("Color of this car is", self.color)
        print("Brand of this car is", self.brand)
        print("Maxspeed of this car is", self.maxspeed)

    # Deconstructor

    def __del__(self):
        print()
