# Program 7c: BankAccount class with deposit, withdraw, and display methods

class BankAccount:
    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Account No: {self.account_no}")
        print(f"Balance: ₹{self.balance}")
        print()


# Creating object and performing operations
acc = BankAccount("Shriyash", "ACC001", 5000)
print("Initial Details:")
acc.display()

acc.deposit(3000)
acc.display()

acc.withdraw(2000)
acc.display()

acc.withdraw(10000)  # Insufficient balance
