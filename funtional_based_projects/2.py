# Data Store
students = {}

# 1. User Defined: Add
add_student = lambda: (
    students.update({
        input("Enter ID: "): {
            "name": input("Enter Name: "),
            "skills": [s.strip().lower() for s in input("Enter Skills (comma-separated): ").split(",")]
        }
    }),
    print("Student Added.")
)

# 2. User Defined: Modify
def modify_student():
    sid = input("Enter Student ID to modify: ")
    if sid in students:
        name = input("Enter new Name: ")
        skills = [s.strip().lower() for s in input("Enter new Skills: ").split(",")]
        students[sid] = {"name": name, "skills": skills}
        print("Update successful.")
    else:
        print("ID not found.")

# 3. User Defined: Delete
delete_student = lambda: (
    print(f"Removed: {students.pop(input('Enter ID to delete: '), 'ID not found')}")
)

# 4. User Defined: List
def list_all():
    print("\n--- Student Records ---")
    for sid, info in students.items():
        print(f"ID: {sid} | Name: {info['name']} | Skills: {', '.join(info['skills'])}")

# 5. Search By Skill (Lambda Style)
def search_by_skill():
    query = input("Enter Skill To Search: ").lower()
    
    # Lambda processes each (ID, data) pair to see if skill exists in the list
    results = list(filter(lambda item: query in item[1]['skills'], students.items()))
    
    if results:
        print(f"\nStudents with skill '{query}':")
        for sid, info in results:
            print(f"Student ID: {sid} | Student Name: {info['name']}")
    else:
        print("No matches found.")

# Main Application Function
def run_app():
    menu = {
        "1": add_student,
        "2": modify_student,
        "3": delete_student,
        "4": list_all,
        "5": search_by_skill
    }
    
    while True:
        print("\n1-Add | 2-Modify | 3-Delete | 4-List | 5-Search | 6-Exit")
        choice = input("Choice: ")
        
        if choice == "6":
            print("Goodbye!")
            break
        
        # Execute from menu if valid choice, otherwise print error
        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")

# Execution
if __name__ == "__main__":
    run_app()