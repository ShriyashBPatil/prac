# Program 5e: Simulate ATM withdrawal with InsufficientBalanceError

class InsufficientBalanceError(Exception):
    """Custom exception for insufficient balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient balance! Available: ₹{balance}, Requested: ₹{amount}"
        super().__init__(self.message)


def withdraw(balance, amount):
    """Simulate ATM withdrawal."""
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive!")
    return balance - amount


# ATM Simulation
balance = 10000
print(f"Current Balance: ₹{balance}")

try:
    amount = float(input("Enter withdrawal amount: ₹"))
    new_balance = withdraw(balance, amount)
    print(f"\n✓ Withdrawal successful!")
    print(f"  Amount withdrawn: ₹{amount}")
    print(f"  Remaining balance: ₹{new_balance}")

except InsufficientBalanceError as e:
    print(f"\n✗ Transaction Failed: {e}")

except ValueError as e:
    print(f"\n✗ Invalid Input: {e}")
