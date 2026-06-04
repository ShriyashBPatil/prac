# Program 1a: Calculate Simple Interest using principal, rate, and time

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100

print(f"\nPrincipal: {principal}")
print(f"Rate: {rate}%")
print(f"Time: {time} years")
print(f"Simple Interest: {simple_interest}")
print(f"Total Amount: {principal + simple_interest}")
