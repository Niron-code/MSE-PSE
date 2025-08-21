class Menu:
    @staticmethod
    def main_menu():
        print("\n==== Main Menu ====")
        print("1. Student")
        print("2. Lecturer")
        print("3. Course")
        print("*. Exit")

    @staticmethod
    def student_menu():
        print("\n==== Student Manager ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Delete Student by ID")
        print("#. Main Menu")

    @staticmethod
    def lecturer_menu():
        print("\n==== Lecturer Manager ====")
        print("1. Add Lecturer")
        print("2. View All Lecturers")
        print("3. Search Lecturer by Name")
        print("4. Delete Lecturer by ID")
        print("#. Main Menu")

    @staticmethod
    def course_menu():
        print("\n==== Course Manager ====")
        print("1. Add Course")
        print("2. View All Courses")
        print("3. Search Course by Name")
        print("4. Delete Course by ID")
        print("#. Main Menu")