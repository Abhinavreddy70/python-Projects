from abc import ABC, abstractmethod

# CUSTOM EXCEPTIONS
class StockError(Exception): pass
class AuthError(Exception): pass

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
    def __repr__(self):
        return f"{self.capacity}mAh"

class AppleProduct(ABC):
    def __init__(self, model, price, stock, bat_capacity):
        self.model = model
        self._price = price             # Protected
        self.stock = stock
        self.battery = Battery(bat_capacity) # Composition

    @abstractmethod
    def get_category(self):
        pass

class IPhone(AppleProduct):
    def get_category(self): return "iPhone"

class MacBook(AppleProduct):
    def get_category(self): return "MacBook"