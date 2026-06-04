# Program 8a: Single Inheritance: Person class to Student class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    def display_student(self):
        self.display_person()
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")


# Creating object
s = Student("Shriyash", 20, 101, 85)
print("Student Details (Single Inheritance):")
s.display_student()
