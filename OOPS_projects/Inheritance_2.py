#Banking Security System
import random
import time

# Base Class (Parent)
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = random.randint(10000, 99999)

    def deposit(self, amount):
        self.balance += amount
        print(f"[{self.account_number}] Deposit successful: +${amount}")
        self.display_balance()

    def display_balance(self):
        print(f"Current Balance for {self.account_holder}: ${self.balance}")

# Child Class 1: Savings Account (Inheritance)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate=0.02):
        # Inherit name and balance from BankAccount
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Real-time Interest Applied: +${interest:.2f}")

# Child Class 2: Checking Account (Inheritance)
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = limit

    def withdraw(self, amount):
        # Specialized logic: Checking if withdrawal exceeds balance + limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"[{self.account_number}] Withdrawal successful: -${amount}")
        else:
            print("Transaction Denied: Insufficient funds (Overdraft limit reached).")
        self.display_balance()

# --- Simulation Logic ---

def start_banking_app():
    print("--- Welcome to Python Central Bank ---")
    
    # Create inherited objects
    user_savings = SavingsAccount("Alice", 1000)
    user_checking = CheckingAccount("Bob", 200)

    # Simulate real-time activity
    print(f"\nProcessing Alice's Savings...")
    time.sleep(1) # Using 'time' to simulate network delay
    user_savings.deposit(500)
    user_savings.apply_interest()

    print(f"\nProcessing Bob's Checking...")
    time.sleep(1)
    user_checking.withdraw(600)  # Uses overdraft logic
    user_checking.withdraw(1000) # Should fail

if __name__ == "__main__":
    start_banking_app()