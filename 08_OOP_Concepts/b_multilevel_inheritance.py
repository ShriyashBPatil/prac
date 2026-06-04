# Program 8b: Multilevel Inheritance: Animal -> Dog -> Puppy

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking. Woof!")


class Puppy(Dog):
    def __init__(self, name, breed, age_months):
        super().__init__(name, breed)
        self.age_months = age_months

    def play(self):
        print(f"{self.name} the {self.breed} puppy ({self.age_months} months old) is playing!")


# Creating object
p = Puppy("Buddy", "Golden Retriever", 3)
print("Multilevel Inheritance: Animal -> Dog -> Puppy")
print("-" * 40)
p.eat()       # From Animal
p.bark()      # From Dog
p.play()      # From Puppy
