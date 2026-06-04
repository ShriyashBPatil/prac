# Program 4c: Find square root, factorial, and power using the math module

import math

num = float(input("Enter a number: "))

print(f"\nSquare root of {num}: {math.sqrt(num)}")
print(f"Factorial of {int(num)}: {math.factorial(int(num))}")
print(f"{num} raised to power 3: {math.pow(num, 3)}")
print(f"Ceiling of {num}: {math.ceil(num)}")
print(f"Floor of {num}: {math.floor(num)}")
print(f"Value of Pi: {math.pi}")
print(dir(math))