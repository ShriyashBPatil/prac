# Program 4a: Display the current date and time using the datetime module

from datetime import datetime

now = datetime.now()

print("Current Date and Time:")
print(f"  Date & Time: {now}")
print(f"  Date: {now.strftime('%d-%m-%Y')}")
print(f"  Time: {now.strftime('%H:%M:%S')}")
print(f"  Day: {now.strftime('%A')}")
print(f"  Month: {now.strftime('%B')}")
print(f"  Year: {now.year}")
