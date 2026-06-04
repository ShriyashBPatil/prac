# Program 4h: Check whether characters are alphabets or digits using string module

import string

text = input("Enter a string: ")

print(f"\nAnalysis of: '{text}'")
print("-" * 30)

for char in text:
    if char in string.ascii_letters:
        print(f"  '{char}' -> Alphabet")
    elif char in string.digits:
        print(f"  '{char}' -> Digit")
    elif char in string.punctuation:
        print(f"  '{char}' -> Punctuation")
    elif char in string.whitespace:
        print(f"  '{char}' -> Whitespace")
    else:
        print(f"  '{char}' -> Other")
