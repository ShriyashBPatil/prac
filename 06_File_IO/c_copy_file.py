# Program 6c: Copy contents from source.txt to target.txt

# Create source file
with open("source.txt", "w") as f:
    f.write("This is the content of source file.\nLine 2 of source.\nLine 3 of source.")

# Copy from source.txt to target.txt
with open("source.txt", "r") as source:
    content = source.read()

with open("target.txt", "w") as target:
    target.write(content)

print("Contents copied from 'source.txt' to 'target.txt' successfully!")

# Verify by reading target file
print("\nContents of 'target.txt':")
with open("target.txt", "r") as f:
    print(f.read())
