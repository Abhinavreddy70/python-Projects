#Personal Banking System

class BankAccount:
    """
    A class demonstrating Encapsulation by protecting the balance 
    from unauthorized external access.
    """
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        
        # PRIVATE ATTRIBUTE: The double underscore (__) makes this 'private'.
        # It cannot be accessed directly outside the class.
        self.__balance = initial_balance 

    # GETTER METHOD: Allows controlled access to read the private data
    def get_balance(self):
        return self.__balance

    # SETTER METHOD (Deposit): Allows controlled modification with logic
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive.")

    # SETTER METHOD (Withdraw): Adds security checks before modifying data
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        elif amount > self.__balance:
            print("Error: Insufficient funds!")
        else:
            print("Error: Withdrawal amount must be positive.")

# ==========================================
# TESTING ENCAPSULATION
# ==========================================
if __name__ == "__main__":
    # 1. Initialize Account
    my_account = BankAccount("Alex", 1000)
    print(f"Account Holder: {my_account.account_holder}")

    # 2. Accessing data the CORRECT way
    print(f"Initial Balance: ${my_account.get_balance()}")

    # 3. Modifying data via secure methods
    my_account.deposit(500)
    my_account.withdraw(200)

    print("\n--- ATTACKING THE DATA (Security Test) ---")

    # 4. Attempting to access the private variable directly (Will fail)
    try:
        print(my_account.__balance)
    except AttributeError:
        print("SECURITY ALERT: Cannot access '__balance' directly from outside.")

    # 5. Attempting to bypass logic and manually set a fake balance
    my_account.__balance = 9999999  # This actually creates a NEW variable, doesn't change the real one
    print(f"Fake balance set by user: {my_account.__balance}")
    print(f"Actual Bank Secure Balance: ${my_account.get_balance()}")