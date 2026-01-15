import data_handler
import validators
from datetime import datetime

def register_student(students):
    try:
        s_id = input("Enter Student ID (e.g., S101): ").strip()
        validators.validate_student_id(s_id, students)
        
        name = input("Enter Student Name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        # Data stored as a nested dictionary (Functional approach)
        students[s_id] = {
            "name": name,
            "courses": {},
            "registration_date": str(datetime.now().date())
        }
        
        data_handler.write_students(students)
        print(f"Student {name} registered successfully!")

    except validators.ValidationError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

def add_grade(students):
    try:
        s_id = input("Enter Student ID: ")
        if s_id not in students:
            raise KeyError(f"Student ID {s_id} not found.")

        course = input("Enter Course Name: ").strip()
        score = float(input("Enter Score: "))
        
        validators.validate_score(score)

    # Updating nested dictionary

        students[s_id]["courses"][course] = score
        data_handler.write_students(students)
        print(f"Grade updated for {students[s_id]['name']}.")

    except KeyError as ke:
        print(f"Search Error: {ke}")
    except validators.ValidationError as ve:
        print(f"Validation Error: {ve}")
    except ValueError:
        print("Error: Please enter a numeric value for the score.")

def display_report(students):
    print("\n" + "="*40)
    print(f"{'ID':<10} {'NAME':<15} {'AVERAGE':<10}")
    print("-" * 40)

    for s_id, info in students.items():
        grades = info["courses"].values()
        
    # Using built-in functions: sum(), len(), round()

        avg = round(sum(grades) / len(grades), 2) if grades else 0.0
        print(f"{s_id:<10} {info['name']:<15} {avg:<10}%")
    print("="*40)

def main():
    data_handler.initialize_db()
    
    while True:
        students = data_handler.read_students()
        
        print("\n--- STUDENT LMS (Functional Version) ---")
        print("1. Register Student")
        print("2. Add/Update Grade")
        print("3. View Performance Report")
        print("4. Exit")
        
        choice = input("Select Option: ")

        if choice == '1':
            register_student(students)
        elif choice == '2':
            add_grade(students)
        elif choice == '3':
            display_report(students)
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()