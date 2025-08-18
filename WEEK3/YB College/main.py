from database import create_table
from lecturer_manager import Lecturer
from student_manager import add_student, view_students, search_student, delete_student

def main_menu():
    print("\n==== Main Menu ====")
    print("1. Student")
    print("2. Lecturer")
    print("*. Exit")

def student_menu():
    print("\n==== Student Manager ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Delete Student by ID")
    print("#. Main Menu")

def lecturer_menu():
    print("\n==== Lecturer Manager ====")
    print("1. Add Lecturer")
    print("2. View All Lecturers")
    print("3. Search Lecturer by Name")
    print("4. Delete Lecturer by ID")
    print("#. Main Menu")

def main():
    create_table()
    while True:
        main_menu()
        choice = input("Select an option (1/2/*): ")
        if choice == '1':
            while True:
                student_menu()
                s_choice = input("Select an option (1-4/#): ")
                if s_choice == '1':
                    name = input("Enter student name: ")
                    address = input("Enter student address: ")
                    add_student(name, address)
                elif s_choice == '2':
                    students = view_students()
                    for student in students:
                        print(student)
                elif s_choice == '3':
                    name = input("Enter student name to search: ")
                    students = search_student(name)
                    for student in students:
                        print(student)
                elif s_choice == '4':
                    student_id = int(input("Enter student ID to delete: "))
                    delete_student(student_id)
                elif s_choice == '#':
                    break
                else:
                    print("Invalid choice, try again.")
        elif choice == '2':
            while True:
                lecturer_menu()
                l_choice = input("Select an option (1-4/#): ")
                if l_choice == '1':
                    name = input("Enter lecturer name: ")
                    email = input("Enter lecturer email: ")
                    Lecturer.add_lecturer(name, email)
                elif l_choice == '2':
                    lecturers = Lecturer.view_lecturers()
                    for lecturer in lecturers:
                        print(lecturer)
                elif l_choice == '3':
                    name = input("Enter lecturer name to search: ")
                    lecturers = Lecturer.search_lecturer(name)
                    for lecturer in lecturers:
                        print(lecturer)
                elif l_choice == '4':
                    lecturer_id = int(input("Enter lecturer ID to delete: "))
                    Lecturer.delete_lecturer(lecturer_id)
                elif l_choice == '#':
                    break
                else:
                    print("Invalid choice, try again.")
        elif choice == '*':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
