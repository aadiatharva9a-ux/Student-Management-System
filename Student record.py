import json

file_name = "students.json"

def load_students():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return []

def save_students(students):
    with open(file_name, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    students = load_students()

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")

def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\nStudent Records:")
    for s in students:
        print(
            "Name:", s["name"],
            "| Roll:", s["roll"],
            "| Course:", s["course"]
        )

def search_student():
    roll = input("Enter roll number to search: ")

    students = load_students()

    for s in students:
        if s["roll"] == roll:
            print("Student Found:")
            print(
                "Name:", s["name"],
                "| Course:", s["course"]
            )
            return

    print("Student not found.")

def update_student():
    roll = input("Enter roll number to update: ")

    students = load_students()

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["course"] = input("Enter new course: ")

            save_students(students)

            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")

    students = load_students()

    new_students = []

    for s in students:
        if s["roll"] != roll:
            new_students.append(s)

    save_students(new_students)

    print("Student deleted successfully!")

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")

menu()