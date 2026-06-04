# Program 3e: Filter even numbers from a list using lambda function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f"Original List: {numbers}")

# Using filter() with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Even Numbers: {even_numbers}")
