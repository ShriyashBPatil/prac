# Program 4d: Generate a random number between 1 and 100

import random

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

# Generate multiple random numbers
print("\n5 Random numbers between 1 and 100:")
for i in range(5):
    print(f"  {random.randint(1, 100)}")
