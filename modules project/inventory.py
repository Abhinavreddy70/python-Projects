# inventory.py

def get_luxury_stock():
    """Returns a list of dictionaries containing car details."""
    return [
        {"id": 1, "brand": "Rolls-Royce", "model": "Phantom", "price": 460000},
        {"id": 2, "brand": "Ferrari", "model": "SF90", "price": 511000},
        {"id": 3, "brand": "Lamborghini", "model": "Revuelto", "price": 608000},
        {"id": 4, "brand": "Bentley", "model": "Continental GT", "price": 240000}
    ]

def find_car_by_id(car_id):
    """Searches for a specific car dictionary by its ID."""
    stock = get_luxury_stock()
    for car in stock:
        if car["id"] == car_id:
            return car
    return None