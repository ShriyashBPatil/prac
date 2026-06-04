# Program 2d: Create a dictionary and display keys and values

student = {
    "name": "Shriyash",
    "roll_no": 101,
    "branch": "Computer Science",
    "marks": 85,
    "city": "Mumbai"
}

print("Student Dictionary:")
print(student)

# Display keys
print("\nKeys:")
for key in student.keys():
    print(f"  {key}")

# Display values
print("\nValues:")
for value in student.values():
    print(f"  {value}")

# Display key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")
