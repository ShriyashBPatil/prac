# Program 3h: Return the sum and average of numbers using a function

def sum_and_average(numbers):
    """Return the sum and average of a list of numbers."""
    total = sum(numbers)
    average = total / len(numbers)
    return total, average


num_list = [10, 20, 30, 40, 50]
print(f"Numbers: {num_list}")

total, avg = sum_and_average(num_list)
print(f"Sum: {total}")
print(f"Average: {avg}")
