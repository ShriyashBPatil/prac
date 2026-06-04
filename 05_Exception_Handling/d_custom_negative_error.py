# Program 5d: Custom exception: NegativeNumberError for negative inputs

class NegativeNumberError(Exception):
    """Custom exception for negative number inputs."""
    def __init__(self, value):
        self.value = value
        self.message = f"Negative number not allowed: {value}"
        super().__init__(self.message)


def check_positive(number):
    """Check if a number is positive, raise error if negative."""
    if number < 0:
        raise NegativeNumberError(number)
    return f"{number} is a positive number"


try:
    num = float(input("Enter a positive number: "))
    result = check_positive(num)
    print(result)

except NegativeNumberError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Please enter a valid number!")
