# Program 2g: Remove duplicate elements from a list using set

my_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5, 8, 1, 9, 4]
print(f"Original List: {my_list}")
print(f"Length (with duplicates): {len(my_list)}")

# Remove duplicates using set
unique_list = list(set(my_list))

print(f"\nList after removing duplicates: {unique_list}")
print(f"Length (without duplicates): {len(unique_list)}")
print(f"Duplicates removed: {len(my_list) - len(unique_list)}")
