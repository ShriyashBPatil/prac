# Program 2b: Create a tuple and display its elements

my_tuple = (10, 20, 30, 40, 50)
print(f"Tuple: {my_tuple}")
print(f"Length: {len(my_tuple)}")

# Accessing elements
print(f"\nFirst element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Slice (1:4): {my_tuple[1:4]}")

# Displaying all elements using loop
print("\nAll elements:")
for index, element in enumerate(my_tuple):
    print(f"  Index {index}: {element}")

# Tuple operations
print(f"\nMaximum: {max(my_tuple)}")
print(f"Minimum: {min(my_tuple)}")
print(f"Sum: {sum(my_tuple)}")
print(f"Count of 30: {my_tuple.count(30)}")
print(f"Index of 40: {my_tuple.index(40)}")
