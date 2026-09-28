from auth import register, login
from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    import_students,
    export_students
)

def student_menu():
    while True:
        print("""
========= STUDENT MANAGEMENT =========
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Import Students (from CSV)
7. Export Students (to CSV)
8. Logout
======================================""")

        choice = input("Enter choice: ").strip()

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
            import_students()
        elif choice == "7":
            export_students()
        elif choice == "8":
            print("Logged out successfully!")
            break
        else:
            print("Invalid choice! Please enter 1-8.")

def main():
    while True:
        print("""
====== STUDENT MANAGEMENT SYSTEM ======
1. Register
2. Login
3. Exit
========================================""")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                student_menu()
        elif choice == "3":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice! Please enter 1-3.")

if __name__ == "__main__":
    main()