# Program 6e: Store details of 3 students into a CSV file

import csv

# Student data
students = [
    ["Roll No", "Name", "Branch", "Marks"],
    [101, "Shriyash", "Computer Science", 85],
    [102, "Rahul", "IT", 90],
    [103, "Priya", "Electronics", 78],
]

# Writing to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("Student details stored in 'students.csv' successfully!")

# Reading and displaying
print("\nContents of students.csv:")
print("-" * 50)
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
