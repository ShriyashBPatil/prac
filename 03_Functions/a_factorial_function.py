# Program 3a: Use a user-defined function to find the factorial of a number

def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is: {factorial(num)}")
