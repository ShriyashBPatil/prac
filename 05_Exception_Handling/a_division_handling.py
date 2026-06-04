# Program 5a: Division program handling ZeroDivision and non-numeric input

try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = num1 / num2
    print(f"\n{num1} / {num2} = {result}")

except ZeroDivisionError:
    print("\nError: Cannot divide by zero!")

except ValueError:
    print("\nError: Please enter numeric values only!")

except Exception as e:
    print(f"\nUnexpected error: {e}")
