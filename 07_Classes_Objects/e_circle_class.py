# Program 7e: Circle class to calculate area and circumference

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def display(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area():.2f}")
        print(f"Circumference: {self.circumference():.2f}")


# Creating object
c = Circle(7)
print("Circle Details:")
c.display()
