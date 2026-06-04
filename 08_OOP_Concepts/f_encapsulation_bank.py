# Program 8f: Encapsulation: BankAccount with private balance variable

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print("Invalid amount or insufficient balance.")

    def get_balance(self):
        return self.__balance

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: ₹{self.__balance}")


# Creating object
acc = BankAccount("Shriyash", 5000)
print("Encapsulation Example (Private Balance):")
print("-" * 40)
acc.display()

acc.deposit(3000)
acc.display()

acc.withdraw(2000)
acc.display()

# Trying to access private variable directly
print(f"\nAccessing via getter: ₹{acc.get_balance()}")
