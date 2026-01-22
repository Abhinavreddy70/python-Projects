import database
from models import IPhone, MacBook, StockError, AuthError

class AppleStoreManager:
    def __init__(self):
        self.__revenue = 0.0 # Encapsulation
        self.inventory_data = database.load_data()

    def process_sale(self, model_name, qty):
        try:
            if model_name not in self.inventory_data:
                print("Product not found!")
                return

            item = self.inventory_data[model_name]
            
            # Check Stock
            if item['stock'] < qty:
                raise StockError(f"Insufficient Stock! Only {item['stock']} left.")

            # Calculate Price
            total = item['price'] * qty
            self.__revenue += total
            
            # Update Local Data and JSON
            self.inventory_data[model_name]['stock'] -= qty
            database.save_data(self.inventory_data)
            
            print(f"Sold {qty} units of {model_name}. Total: ${total}")

        except StockError as e:
            print(f"Error: {e}")

    def show_report(self, pin):
        if pin != "1234":
            print("Unauthorized!")
            return
        print(f"Total Sales Revenue: ${self.__revenue}")

if __name__ == "__main__":
    store = AppleStoreManager()
    
    print("--- Welcome to Apple Modular System ---")
    store.process_sale("iPhone 15", 2)
    store.process_sale("MacBook M3", 1)
    
    print("\n--- Final Report ---")
    store.show_report("1234")