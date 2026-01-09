# Initial Data Store
students = {
    "S01": {"name": "Alice", "skills": ["Python", "Data Science"]},
    "S02": {"name": "Bob", "skills": ["Java", "React"]},
    "S03": {"name": "Charlie", "skills": ["Python", "SQL"]}
}

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    skills = input("Enter Skills (comma separated): ").split(",")
    students[sid] = {"name": name.strip(), "skills": [s.strip() for s in skills]}
    print(f"Student {sid} added successfully.")

def modify_student():
    sid = input("Enter Student ID to modify: ")
    if sid in students:
        name = input("Enter new Name: ")
        skills = input("Enter new Skills (comma separated): ").split(",")
        students[sid] = {"name": name.strip(), "skills": [s.strip() for s in skills]}
        print("Record updated.")
    else:
        print("Student ID not found.")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    if students.pop(sid, None):
        print(f"Student {sid} removed.")
    else:
        print("Student ID not found.")

def list_students():
    print("\n--- Current Student List ---")
    for sid, info in students.items():
        print(f"ID: {sid} | Name: {info['name']} | Skills: {', '.join(info['skills'])}")

def search_by_skill():
    search_term = input("Enter Skill To Search: ").lower()
    
    # Lambda Style: Filtering the dictionary items based on the skill list
    # We use a lambda to check if the search_term exists in the skills list
    results = filter(lambda item: search_term in [s.lower() for s in item[1]['skills']], students.items())
    
    print(f"\nResults for '{search_term}':")
    found = False
    for sid, info in results:
        print(f"Student ID: {sid} | Student Name: {info['name']}")
        found = True
    
    if not found:
        print("No students found with that skill.")

def main():
    while True:
        print("\n--- Student Management Menu ---")
        print("1 - Add Student")
        print("2 - Modify Student")
        print("3 - Delete Student")
        print("4 - List All Students")
        print("5 - Search By Skill (Lambda)")
        print("6 - Exit App")
        
        choice = input("Choose an option: ")
        
        if choice == '1': add_student()
        elif choice == '2': modify_student()
        elif choice == '3': delete_student()
        elif choice == '4': list_students()
        elif choice == '5': search_by_skill()
        elif choice == '6': 
            print("Exiting app...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()





   # Feature,Python Implementation
#Data Storage,"A nested dictionary ({ID: {name: """", skills: []}}) allows for quick O(1) lookups."
#Built-in Functions,"Used input(), print(), split(), and strip() for data handling."
#Lambda Function,Used inside filter() to scan the nested skill lists without a traditional for loop.
#Dictionary pop(),Used in the Delete function to remove a key and handle missing keys gracefully in one line.