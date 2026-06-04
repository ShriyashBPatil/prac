# Program 4e: Generate a random password of length 8

import random
import string

def generate_password(length=8):
    """Generate a random password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password = generate_password(8)
print(f"Generated Random Password (length 8): {password}")
