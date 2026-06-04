# Program 3c: Add two numbers using a function

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = add_numbers(num1, num2)
print(f"\nSum of {num1} and {num2} is: {result}")
