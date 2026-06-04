# Program 2a: Perform list operations; find maximum and minimum values in a list

my_list = [45, 12, 78, 34, 56, 89, 23, 67]
print(f"Original List: {my_list}")

# List Operations
my_list.append(100)
print(f"After append(100): {my_list}")

my_list.insert(2, 50)
print(f"After insert(2, 50): {my_list}")

my_list.remove(34)
print(f"After remove(34): {my_list}")

my_list.sort()
print(f"After sort(): {my_list}")

my_list.reverse()
print(f"After reverse(): {my_list}")

# Maximum and Minimum
print(f"\nMaximum value: {max(my_list)}")
print(f"Minimum value: {min(my_list)}")
print(f"Sum of list: {sum(my_list)}")
print(f"Length of list: {len(my_list)}")
