# Base/Parent class - Contains common attributes for all persons
class Person:
    def __init__(self, name, address, age, id):
        self.name = name
        self.address = address
        self.age = age
        self.id = id

# Student inherits from Person (Child class)
# Inherits all attributes from Person and adds academic_record
class Student(Person):
    def __init__(self, name, address, age, id, academic_record):
        # super() calls the parent class's __init__ method
        super().__init__(name, address, age, id)
        self.academic_record = academic_record

# Staff inherits from Person (Child class)
# Inherits all attributes from Person and adds tax_code
class Staff(Person):
    def __init__(self, name, address, age, id, tax_code):
        super().__init__(name, address, age, id)
        self.tax_code = tax_code

# Academic inherits from Staff (Multilevel inheritance)
# Inherits all attributes from Staff (and Person) and adds salary
class Academic(Staff):
    def __init__(self, name, address, age, id, tax_code, salary):
        super().__init__(name, address, age, id, tax_code)
        self.salary = salary

# General inherits from Staff (Multilevel inheritance)
# Inherits all attributes from Staff (and Person) and adds pay_rate
class General(Staff):
    def __init__(self, name, address, age, id, tax_code, pay_rate):
        super().__init__(name, address, age, id, tax_code)
        self.pay_rate = pay_rate

# Example usage:
if __name__ == "__main__":
    # Creates instances of different classes showing inheritance hierarchy:
    # Student inherits from Person
    student = Student("John Doe", "123 Student St", 20, "S001", {"GPA": 3.8})
    
    # Academic inherits from Staff which inherits from Person
    academic = Academic("Dr. Smith", "456 Prof Ave", 45, "A001", "T123", 75000)
    
    # General inherits from Staff which inherits from Person
    staff = General("Jane Wilson", "789 Staff Rd", 35, "G001", "T456", 25.50)