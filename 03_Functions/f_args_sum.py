# Program 3f: Calculate the sum of multiple numbers using *args

def sum_numbers(*args):
    """Calculate the sum of multiple numbers using *args."""
    total = sum(args)
    print(f"Numbers: {args}")
    print(f"Sum: {total}")
    return total


print("Test 1:")
sum_numbers(10, 20, 30)

print("\nTest 2:")
sum_numbers(5, 15, 25, 35, 45)

print("\nTest 3:")
sum_numbers(100, 200)
