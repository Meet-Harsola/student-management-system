from database import initialize_database
from student_manager import StudentManager
import sqlite3


def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 40)
    print("        Student Management System")
    print("\n" + "=" * 40)

    print("1. Add Student ")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
 
    print("\n" + "=" * 40)

def add_student_menu(manager):
    """Collect student and register a student."""

    print("\n --- Add Student ---")

    student_id = input("Enter Student ID : ")
    name = input("Enter Student Name : ")
    age = input("Enter Student Age : ")
    course = input("Enter Student Course: ")
    email = input ("Enter Student Email : ")

    success, message = manager.add_student(
        student_id,
        name,
        age,
        course,
        email
    )

    print(message)

def view_all_students_menu(manager):
    """Display all registered students."""

    print("\n --- ALL STUDENTS ---")

    students = manager.get_all_students()

    if not students:
        print ("No students registered yet.")
        return 
    
    print("-" * 90)
    print(
        f"{'ID':<10}"
        f"{'Name':<25}"
        f"{'Age' :<8}"
        f"{'Course':<25}"
        f"{'Email':<25}"
    )

    print("-"*90)

    for student in students:
        print(
            f"{student[0]:<10}"
            f"{student[1]:<25}"
            f"{student[2]:<8}"
            f"{student[3]:<25}"
            f"{student[4]:<25}"
        )
    print("-"*90)

def search_student_menu(manager):
    """Search for a student using their ID."""

    print("\n --- Search Student --- ")

    student_id = input("Enter student ID : ").strip()

    student = manager.get_student(student_id)

    if student is None:
        print("Student not Found.")
        return 
    
    print("\n Student Details")
    print("-"*30)

    print(f"Student ID  : {student[0]}")
    print(f"Name        : {student[1]}")
    print(f"Age         : {student[2]}")
    print(f"Course      : {student[3]}")
    print(f"Email       : {student[4]}")


def update_student_menu(manager):
    """Update an Existing student information."""

    print("\n ---- Update Student ----")

    student_id = input("Enter Student ID to update: ").strip()

    student = manager.get_student(student_id)

    if student is None:
        print("Student Not Found.")
        return 
    
    print("\n Current Student Details")
    print(f"Name     : {student[1]}")
    print(f"Age      : {student[2]}")
    print(f"Course   : {student[3]}")
    print(f"Email    : {student[4]}")

    print("\n Enter the new Details.")

    name = input("Enter new Name : ")
    age = input("Enter new age : ")
    course = input("Enter new curse : ")
    email = input("Enter new email : ")

    success, message = manager.update_student(
        student_id,
        name,
        age,
        course,
        email
    )

    print(message)


def delete_student_menu(manager):
    """Delete a student after confirmation."""

    print("\n --- Delete Student --- ")

    student_id = input("Enter Student ID to delete: ").strip()

    student = manager.get_student(student_id)

    if student is None:
        print("Student not Found.")
        return 
    
    print("\n Student Details")
    print(f"ID       :{student[0]}")
    print(f"Name     : {student[1]}")
    print(f"Course   : {student[3]}")

    confirmation = input (
        "Are you sure you want to delete this student? (yes/no) : "
    ).strip().lower()

    if confirmation != "yes":
        print("Deletion cancelled.")
        return 
    
    success, message = manager.delete_student(student_id)

    print(message)
    
    





def main():
    """Run the Student Management System."""

    try:
        initialize_database()
    except sqlite3.Error:
        print("Unable to initialize the database. Please check your setup.")
        return
    
    manager = StudentManager()

    while True:
        display_menu()

        choice = input("Enter your choice(1-6): ").strip()

        if choice == "1":
            add_student_menu(manager)
        
        elif choice == "2":
            view_all_students_menu(manager)

        elif choice == "3":
            search_student_menu(manager)
        
        elif choice == "4":
            update_student_menu(manager)
        
        elif choice == "5":
            delete_student_menu(manager)

        elif choice == "6":
            print("\nThank You for using Student Management System!")
            break

        else:
            print("\nInvalid Choice. Please enter the number form 1 to 6.")

if __name__ == "__main__":
    main()