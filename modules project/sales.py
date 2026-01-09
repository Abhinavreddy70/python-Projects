# sales.py

def calculate_total(price, tax_rate=0.10):
    """Calculates the tax and the final total price."""
    tax_amount = price * tax_rate
    total = price + tax_amount
    return tax_amount, total

def generate_invoice(customer_name, car_dict):
    """Formats and prints the final sale details."""
    price = car_dict["price"]
    tax, total = calculate_total(price)

    print("\n" + "="*30)
    print("      OFFICIAL INVOICE")
    print("="*30)
    print(f"Customer: {customer_name}")
    print(f"Vehicle:  {car_dict['brand']} {car_dict['model']}")
    print(f"Base:     ${price:,}")
    print(f"Tax:      ${tax:,.2f}")
    print("-" * 30)
    print(f"TOTAL:    ${total:,.2f}")
    print("="*30)