# Program 1e: Calculate the factorial of a given number using a loop

num = int(input("Enter a number: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"\nFactorial of {num} is: {factorial}")
