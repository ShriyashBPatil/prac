# Program 2c: Perform union and intersection of two sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union
union_result = set1 | set2  # or set1.union(set2)
print(f"\nUnion (set1 | set2): {union_result}")

# Intersection
intersection_result = set1 & set2  # or set1.intersection(set2)
print(f"Intersection (set1 & set2): {intersection_result}")

# Difference
difference_result = set1 - set2  # or set1.difference(set2)
print(f"Difference (set1 - set2): {difference_result}")

# Symmetric Difference
sym_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print(f"Symmetric Difference (set1 ^ set2): {sym_diff}")
