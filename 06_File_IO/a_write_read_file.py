# Program 6a: Write a paragraph to data.txt and then read/display it

# Writing to file
paragraph = """Python is a versatile programming language known for its simplicity and readability.
It is widely used in web development, data science, artificial intelligence, and automation.
Python's extensive library support makes it one of the most popular languages in the world."""

with open("data.txt", "w") as file:
    file.write(paragraph)
print("Data written to 'data.txt' successfully!")

# Reading from file
print("\nReading from 'data.txt':")
print("-" * 50)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
