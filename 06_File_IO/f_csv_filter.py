# Program 6f: Read CSV and display students with marks > 75

import csv

# First create a CSV file with student data
students = [
    ["Roll No", "Name", "Branch", "Marks"],
    [101, "Shriyash", "Computer Science", 85],
    [102, "Rahul", "IT", 90],
    [103, "Priya", "Electronics", 60],
    [104, "Amit", "Mechanical", 78],
    [105, "Neha", "Civil", 55],
]

with open("marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

# Read CSV and filter students with marks > 75
print("Students with Marks > 75:")
print("-" * 50)

with open("marks.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header
    print(f"{'Roll No':<10}{'Name':<15}{'Branch':<20}{'Marks':<10}")
    print("-" * 50)
    for row in reader:
        if int(row[3]) > 75:
            print(f"{row[0]:<10}{row[1]:<15}{row[2]:<20}{row[3]:<10}")
