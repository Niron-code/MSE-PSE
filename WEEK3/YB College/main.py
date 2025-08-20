from database import create_table
from lecturer_manager import Lecturer
from student_manager import Student
from menu import Menu

def main():
    create_table()
    while True:
        Menu.main_menu()
        choice = input("Select an option (1/2/*): ")
        if choice == '1':
            while True:
                Menu.student_menu()
                s_choice = input("Select an option (1-4/#): ")
                if s_choice == '1':
                    name = input("Enter student name: ")
                    address = input("Enter student address: ")
                    Student.add_student(name, address)
                elif s_choice == '2':
                    students = Student.view_students()
                    for student in students:
                        print(student)
                elif s_choice == '3':
                    name = input("Enter student name to search: ")
                    students = Student.search_student(name)
                    for student in students:
                        print(student)
                elif s_choice == '4':
                    student_id = int(input("Enter student ID to delete: "))
                    Student.delete_student(student_id)
                elif s_choice == '#':
                    break
                else:
                    print("Invalid choice, try again.")
        elif choice == '2':
            while True:
                Menu.lecturer_menu()
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
