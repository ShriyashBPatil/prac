# Program 6d: Store and read student marks using a binary file

import pickle

# Student data
students = [
    {"name": "Shriyash", "roll_no": 101, "marks": 85},
    {"name": "Rahul", "roll_no": 102, "marks": 90},
    {"name": "Priya", "roll_no": 103, "marks": 78},
]

# Writing to binary file
with open("students.dat", "wb") as file:
    pickle.dump(students, file)
print("Student data written to 'students.dat' (binary file)")

# Reading from binary file
with open("students.dat", "rb") as file:
    loaded_students = pickle.load(file)

print("\nStudent Data read from binary file:")
print("-" * 40)
for student in loaded_students:
    print(f"  Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}")
