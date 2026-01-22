import json
import os

DB_FILE = "apple_inventory.json"

def load_data():
    """Loads inventory from JSON file."""
    if not os.path.exists(DB_FILE):
        # Initial dummy data if file doesn't exist
        return {
            "iPhone 15": {"price": 999, "stock": 10, "battery": 3200},
            "MacBook M3": {"price": 1299, "stock": 5, "battery": 5000}
        }
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)