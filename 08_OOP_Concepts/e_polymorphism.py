# Program 8e: Polymorphism: Bird and Airplane both using fly() method

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} flies by flapping its wings.")


class Airplane:
    def __init__(self, model):
        self.model = model

    def fly(self):
        print(f"{self.model} flies using jet engines.")


# Polymorphism in action
def make_it_fly(obj):
    obj.fly()


print("Polymorphism Example:")
print("-" * 40)

bird = Bird("Eagle")
plane = Airplane("Boeing 747")

make_it_fly(bird)
make_it_fly(plane)
