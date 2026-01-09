import time
import random

# Level 1: The Base Class (Parent)
class Vehicle:
    def __init__(self, vehicle_id, driver_name):
        self.vehicle_id = vehicle_id
        self.driver_name = driver_name
        self.status = "Idle"
        self.location = (0, 0)

    def update_location(self):
        # Simulating real-time GPS movement
        self.location = (random.randint(1, 100), random.randint(1, 100))
        print(f"[{self.vehicle_id}] moving to coordinates: {self.location}")

# Level 2: Specialized Class (Child - Inheritance)
class DeliveryVehicle(Vehicle):
    def __init__(self, vehicle_id, driver_name, capacity):
        # Using super() to inherit properties from Vehicle
        super().__init__(vehicle_id, driver_name)
        self.capacity = capacity
        self.current_load = 0

    def load_package(self, weight):
        if self.current_load + weight <= self.capacity:
            self.current_load += weight
            self.status = "In Transit"
            print(f"Loaded {weight}kg. Current load: {self.current_load}/{self.capacity}kg")
        else:
            print("Overweight! Cannot load package.")

# Level 3: Specific Vehicle Types (Grandchildren - Multilevel Inheritance)
class Drone(DeliveryVehicle):
    def fly(self):
        print(f"Drone {self.vehicle_id} is taking off for aerial delivery...")
        self.update_location()

class Truck(DeliveryVehicle):
    def drive(self):
        print(f"Truck {self.vehicle_id} is cruising on the highway...")
        self.update_location()

# --- Real-Time Execution ---

def run_logistics_system():
    print("--- Initializing Logistics Fleet --- \n")
    
    # Instantiate inherited classes
    fast_drone = Drone(vehicle_id="SKY-001", driver_name="AI-Pilot", capacity=10)
    heavy_truck = Truck(vehicle_id="ROAD-99", driver_name="John Doe", capacity=5000)

    # Simulate real-time actions
    fast_drone.load_package(5)
    fast_drone.fly()
    
    print("-" * 30)
    
    heavy_truck.load_package(1200)
    heavy_truck.drive()

if __name__ == "__main__":
    run_logistics_system()