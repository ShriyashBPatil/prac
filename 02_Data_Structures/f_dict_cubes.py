# Program 2f: Create a dictionary of numbers and their cubes

# Using dictionary comprehension
cubes = {x: x ** 3 for x in range(1, 6)}

print("Dictionary of Numbers and their Cubes:")
print("-" * 25)
for number, cube in cubes.items():
    print(f"  {number}^3 = {cube}")

print(f"\nCubes Dictionary: {cubes}")
