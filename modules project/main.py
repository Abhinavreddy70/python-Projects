# main.py
import inventory
import sales

def run_dealership():
    print("--- Welcome to the Functional Luxury Showroom ---")
    
    # 1. Get and display data
    cars = inventory.get_luxury_stock()
    for car in cars:
        print(f"[{car['id']}] {car['brand']} {car['model']} - ${car['price']:,}")

    # 2. User Input
    try:
        choice = int(input("\nEnter the ID of the car you want: "))
        selected_car = inventory.find_car_by_id(choice)

        if selected_car:
            name = input("Enter your name: ")
            # 3. Process the sale
            sales.generate_invoice(name, selected_car)
        else:
            print("Error: Car ID not found.")
            
    except ValueError:
        print("Please enter a valid numeric ID.")

if __name__ == "__main__":
    run_dealership()