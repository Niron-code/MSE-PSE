# Student inherits from Person (Child class)
# Inherits all attributes from Person and adds academic_record
from person import Person


class Student(Person):
    def __init__(self, name, address, age, student_id):
        # super() calls the parent class's __init__ method
        super().__init__(name, address, age)
        self.student_id = student_id

    # Override display_info method
    def display_info(self):
        # Call parent class method using super()
        parent_info = super().display_info()
        # Add student-specific information
        return f"{parent_info}\nStudent ID: {self.student_id}"

# Example use case
student = Student("Philip", "123 Main St", 26, "S12345")
student.address = "Auckland"
print(student.display_info())