#Payment Method Interface-based Polymorphism

from abc import ABC, abstractmethod

# The Interface (Abstract Base Class)
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Implementation 1: Credit Card
class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card ({self.card_number[-4:]})."

# Implementation 2: PayPal
class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal account: {self.email}."

# Implementation 3: Crypto
class Bitcoin(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def process_payment(self, amount):
        return f"Processing ${amount} using Bitcoin wallet {self.wallet_address[:8]}..."

# --- THE POLYMORPHIC ENGINE ---
def checkout(payment_type, amount):
    # This function doesn't care what the payment_type is, 
    # as long as it has a .process_payment() method.
    print(payment_type.process_payment(amount))

# Real-time usage
cart_total = 150.00
user_choice = CreditCard("1234-5678-9012-3456")

checkout(user_choice, cart_total)