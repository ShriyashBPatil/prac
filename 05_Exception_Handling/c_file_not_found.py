# Program 5c: File reading with FileNotFoundError handling and finally block

filename = input("Enter the filename to read: ")

try:
    file = open(filename, "r")
    content = file.read()
    print(f"\nFile Contents:\n{content}")

except FileNotFoundError:
    print(f"\nError: File '{filename}' not found!")

except PermissionError:
    print(f"\nError: Permission denied to read '{filename}'!")

except Exception as e:
    print(f"\nUnexpected error: {e}")

finally:
    print("\n--- File operation completed (finally block executed) ---")
