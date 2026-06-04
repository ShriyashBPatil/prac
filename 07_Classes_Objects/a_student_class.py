# Program 7a: Student class with constructor and display() method

class Student:
    def __init__(self, name, roll_no, branch, marks):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Branch: {self.branch}")
        print(f"Marks: {self.marks}")
        print()


# Creating objects
s1 = Student("Shriyash", 101, "Computer Science", 85)
s2 = Student("Rahul", 102, "IT", 90)

print("Student 1:")
s1.display()

print("Student 2:")
s2.display()
