# Program 1h: Display the multiplication table of a given number

num = int(input("Enter a number: "))

print(f"\nMultiplication Table of {num}:")
print("-" * 20)
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
