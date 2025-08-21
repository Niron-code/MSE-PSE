class Menu:
    @staticmethod
    def main_menu():
        print("Welcome to the Yoobee College Management System")
        print("==== Main Menu ====")
        print("1. Student")
        print("2. Lecturer")
        print("3. Course")
        print("4. Enrollment")
        print("5. Course and Lecturer")
        print("*. Exit")

    @staticmethod
    def student_menu():
        print("\n==== Student Manager ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Delete Student by ID")
        print("5. Update Student")
        print("#. Main Menu")

    @staticmethod
    def lecturer_menu():
        print("\n==== Lecturer Manager ====")
        print("1. Add Lecturer")
        print("2. View All Lecturers")
        print("3. Search Lecturer by Name")
        print("4. Delete Lecturer by ID")
        print("5. Update Lecturer")
        print("#. Main Menu")

    @staticmethod
    def course_menu():
        print("\n==== Course Manager ====")
        print("1. Add Course")
        print("2. View All Courses")
        print("3. Search Course by Name")
        print("4. Delete Course by ID")
        print("5. Update Course")
        print("#. Main Menu")

    @staticmethod
    def enrollment_menu():
        print("\n==== Enrollment Manager ====")
        print("1. Add Enrollment")
        print("2. View All Enrollments")
        print("3. Search Enrollment")
        print("4. Delete Enrollment")
        print("5. Update Enrollment")
        print("#. Main Menu")

    @staticmethod
    def course_lecturer_menu():
        print("\n==== Course Lecturer Manager ====")
        print("1. Add Course Lecturer")
        print("2. View All Course Lecturers")
        print("3. Search Course Lecturer")
        print("4. Delete Course Lecturer")
        print("5. Update Course Lecturer")
        print("#. Main Menu")