# Program 4b: Find the difference between two dates using the datetime module

from datetime import date

date1 = date(2025, 1, 1)
date2 = date(2025, 12, 31)

difference = date2 - date1

print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"\nDifference: {difference.days} days")
