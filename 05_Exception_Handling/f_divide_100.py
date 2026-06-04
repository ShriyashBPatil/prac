# Program 5f: Divide 100 by user input with full error handling

try:
    user_input = input("Enter a number to divide 100 by: ")
    num = float(user_input)
    result = 100 / num
    print(f"\n100 / {num} = {result}")

except ZeroDivisionError:
    print("\nError: Cannot divide by zero!")

except ValueError:
    print(f"\nError: '{user_input}' is not a valid number!")

except Exception as e:
    print(f"\nUnexpected error: {e}")

else:
    print("Division performed successfully!")

finally:
    print("--- Program execution completed ---")
