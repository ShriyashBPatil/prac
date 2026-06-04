# Program 2e: Create a list of squares of numbers from 1 to 5

# Using list comprehension
squares = [x ** 2 for x in range(1, 6)]

print("Numbers and their Squares:")
print("-" * 20)
for i in range(1, 6):
    print(f"  {i}^2 = {i ** 2}")

print(f"\nList of squares: {squares}")
