# Program 5b: Access list element by index with out-of-range handling

my_list = [10, 20, 30, 40, 50]
print(f"List: {my_list}")
print(f"Valid indices: 0 to {len(my_list) - 1}")

try:
    index = int(input("\nEnter the index to access: "))
    value = my_list[index]
    print(f"Element at index {index}: {value}")

except IndexError:
    print(f"\nError: Index out of range! Valid indices are 0 to {len(my_list) - 1}")

except ValueError:
    print("\nError: Please enter a valid integer index!")
