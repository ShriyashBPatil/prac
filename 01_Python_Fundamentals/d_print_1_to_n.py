# Program 1d: Print numbers from 1 to N using a for loop

n = int(input("Enter the value of N: "))

print(f"\nNumbers from 1 to {n}:")
for i in range(1, n + 1):
    print(i, end=" ")
print()
