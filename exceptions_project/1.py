print("="*50)
print("Personal Finance Tracker")
print("="*50)
class InsufficientFundsError(Exception):
    """Custom exception for when the balance is too low."""
    pass

def update_balance():
    filename = "balance.txt"
    
    try:
        # 1. Try to read the current balance
        with open(filename, "r") as file:
            balance = float(file.read())
            
        print(f"Current Balance: ${balance:.2f}")
        
        # 2. Get user input and convert to float
        expense = float(input("Enter the expense amount: "))
        
        # 3. Check for logic errors
        if expense > balance:
            raise InsufficientFundsError(f"You only have ${balance:.2f}")
            
        # 4. Calculate new balance
        balance -= expense
        
        # 5. Write back to file
        with open(filename, "w") as file:
            file.write(str(balance))
        
        print(f"Success! New balance: ${balance:.2f}")

    except FileNotFoundError:
        print("Error: 'balance.txt' not found. Creating a new one with $100.00.")
        with open(filename, "w") as file:
            file.write("100.00")
            
    except ValueError:
        print("Invalid Input: Please enter a numeric value (e.g., 15.50).")
        
    except InsufficientFundsError as e:
        print(f"Transaction Denied: {e}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    finally:
        print("Session ended. Thank you for using Finance Manager.")

# Run the app
update_balance()



#Block,Purpose
#try,"Contains the ""happy path""—the code you want to run if everything goes perfectly."
#except,Catch specific errors so the program doesn't crash. We caught ValueError and FileNotFoundError.
#raise,Manually triggers an error. We used this for our custom logic (Insufficient Funds).
#finally,Runs no matter what happens (success or failure). Perfect for closing files or printing exit messages.