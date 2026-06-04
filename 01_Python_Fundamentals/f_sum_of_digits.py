# Program 1f: Find the sum of digits of a given number using while loop

num = int(input("Enter a number: "))

temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print(f"\nSum of digits of {num} is: {sum_digits}")
