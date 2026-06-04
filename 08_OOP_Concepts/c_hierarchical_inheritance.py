# Program 8c: Hierarchical Inheritance: Shape -> Rectangle and Triangle

class Shape:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Shape: {self.name}")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Creating objects
print("Hierarchical Inheritance: Shape -> Rectangle & Triangle")
print("-" * 50)

rect = Rectangle(10, 5)
rect.display()
print(f"Area: {rect.area()}\n")

tri = Triangle(8, 6)
tri.display()
print(f"Area: {tri.area()}")
