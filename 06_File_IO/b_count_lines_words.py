# Program 6b: Count lines, words, and characters in a text file

# First, create a sample file
sample_text = """Hello World
Python Programming is fun
Learning file operations
This is the fourth line
Python is great"""

with open("sample.txt", "w") as f:
    f.write(sample_text)

# Count lines, words, and characters
with open("sample.txt", "r") as file:
    content = file.read()
    lines = content.split("\n")
    words = content.split()
    characters = len(content)

print(f"File: sample.txt")
print(f"-" * 30)
print(f"Lines: {len(lines)}")
print(f"Words: {len(words)}")
print(f"Characters: {characters}")
