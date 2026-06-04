# Program 4f: Count the number of vowels in a string using the string module

import string

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"\nString: '{text}'")
print(f"Number of vowels: {vowel_count}")
print(f"Vowels found: {[ch for ch in text if ch in vowels]}")
