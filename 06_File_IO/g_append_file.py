# Program 6g: Append a new line of text to an existing file

# Create initial file
with open("append_demo.txt", "w") as f:
    f.write("Line 1: This is the original content.\n")
    f.write("Line 2: Python is great.\n")

print("Original file content:")
with open("append_demo.txt", "r") as f:
    print(f.read())

# Append new line
new_line = "Line 3: This line was appended later.\n"
with open("append_demo.txt", "a") as f:
    f.write(new_line)

print("After appending:")
with open("append_demo.txt", "r") as f:
    print(f.read())
