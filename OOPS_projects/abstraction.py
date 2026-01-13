#Employee Management System

from abc import ABC, abstractmethod

# ==========================================
# 1. THE ABSTRACT BASE CLASS (The Blueprint)
# ==========================================
class Employee(ABC):
    """
    Abstract Base Class. This cannot be instantiated directly.
    It acts as a contract for all subclasses.
    """
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        """Mandatory: Every subclass must define its own salary logic."""
        pass

    @abstractmethod
    def get_position(self):
        """Mandatory: Every subclass must define its own position."""
        pass

    def display_details(self):
        """Shared Method: All employees use this same logic."""
        print(f"[{self.emp_id}] Name: {self.name}")


# ==========================================
# 2. CONCRETE CLASSES (The Implementations)
# ==========================================
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_pay):
        super().__init__(name, emp_id)
        self.monthly_pay = monthly_pay

    def calculate_salary(self):
        return self.monthly_pay

    def get_position(self):
        return "Full-Time Corporate Staff"

class Contractor(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_position(self):
        return "Independent Contractor"


# ==========================================
# 3. DEMONSTRATING ABSTRACTION RULES
# ==========================================
if __name__ == "__main__":
    print("--- 1. SUCCESSFUL IMPLEMENTATION ---")
    # List of different objects treated as the same 'Employee' type
    payroll_list = [
        FullTimeEmployee("John Doe", "FT-101", 5000),
        Contractor("Jane Smith", "CN-202", 50, 160)
    ]

    for emp in payroll_list:
        emp.display_details()
        print(f"Position: {emp.get_position()}")
        print(f"Total Payout: ${emp.calculate_salary()}\n")

    print("--- 2. TESTING ABSTRACTION ENFORCEMENT ---")
    
    # TEST A: Trying to create the Abstract Class itself
    try:
        print("Attempting to create a generic Employee object...")
        generic_emp = Employee("Unknown", "000")
    except TypeError as e:
        print(f"CAUGHT ERROR: {e}")
        print("EXPLANATION: You cannot instantiate an Abstract Class!\n")

    # TEST B: Forgetting a method in a subclass
    try:
        print("Attempting to create an Intern class without 'calculate_salary'...")
        class Intern(Employee):
            def get_position(self):
                return "Intern"
        
        # This line will trigger the error because (calculate_salary is missing)
        junior = Intern("Mark", "IN-501")
    except TypeError as e:
        print(f"CAUGHT ERROR: {e}")
        print("EXPLANATION: Subclasses MUST implement all @abstractmethods.")