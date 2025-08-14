class Employee:
    # Class variable to keep track of employee IDs
    id_counter = 1000  # Starting from 1000

    def __init__(self, name, salary, job_title):
        # Store all data in a list [id, name, job_title, salary]
        self.data = [
            Employee.id_counter,  # ID at index 0
            name,                 # Name at index 1
            job_title,           # Job title at index 2
            salary               # Salary at index 3
        ]
        Employee.id_counter += 1  # Increment for next employee
        self.greet_new_employee()
    
    def greet_new_employee(self):
        print(f"Welcome aboard, {self.data[1]}!")
        print(f"You have been assigned Employee ID: {self.data[0]}")

    def display_info(self):
        print(f"\nEmployee ID: {self.data[0]}")
        print(f"Name: {self.data[1]}")
        print(f"Job Title: {self.data[2]}")
        print(f"Salary: ${self.data[3]:.2f}")

    def give_raise(self, amount):
        self.data[3] += amount  # Update salary in the list (now at index 3)
        print(f"\n{self.data[1]} (ID: {self.data[0]}) received a raise of ${amount:.2f}")
        print(f"New salary: ${self.data[3]:.2f}")


class HRSystem:
    def __init__(self):
        self.employees = []
        self.greet_user()

    def greet_user(self):
        print("\n=== Welcome to the HR Management System ===")
        print("Here you can manage employee information and process raises.")
        print("Let's get started!\n")

    def add_employee(self, name, job_title, salary):
        print("\n=== Adding New Employee ===")
        emp = Employee(name, salary, job_title)
        self.employees.append(emp)
        print("Employee registration completed successfully!")
        return emp

    def display_all_employees(self):
        if not self.employees:
            print("\nNo employees in the system.")
            return
        
        # Define column widths
        id_width = 10
        name_width = 25
        title_width = 25
        salary_width = 15
        total_width = id_width + name_width + title_width + salary_width + 5  # +5 for spacing

        # Print header
        print("\n" + "="*total_width)
        header = (f"| {'ID':^{id_width-2}} | "
                 f"{'Name':^{name_width-2}} | "
                 f"{'Job Title':^{title_width-2}} | "
                 f"{'Salary':^{salary_width-2}} |")
        print(header)
        print("="*total_width)
        
        # Print each employee's data
        for emp in self.employees:
            # Format salary with commas for thousands
            salary = f"${emp.data[3]:,.2f}"
            # Create row with proper spacing and alignment
            row = (f"| {emp.data[0]:^{id_width-2}} | "
                  f"{emp.data[1]:<{name_width-2}} | "
                  f"{emp.data[2]:<{title_width-2}} | "
                  f"{salary:>{salary_width-2}} |")
            print(row)
        
        print("="*total_width)

    def find_employee_by_id(self, emp_id):
        for emp in self.employees:
            if emp.data[0] == emp_id:
                return emp
        return None

    def process_raises(self):
        if not self.employees:
            print("\nNo employees in the system to give raises to.")
            return

        while True:
            while True:
                try:
                    emp_id = int(input("\nEnter employee ID to give raise: "))
                    emp = self.find_employee_by_id(emp_id)
                    if emp:
                        raise_amount = get_valid_salary("Enter raise amount: $")
                        emp.give_raise(raise_amount)
                        break
                    else:
                        print("Employee ID not found! Please try again.")
                except ValueError:
                    print("Please enter a valid number for employee ID.")
            
            while True:
                choice = input("\nDo you want to give another raise? (y/n): ").lower()
                if choice in ['y', 'n']:
                    break
                print("Please enter 'y' for yes or 'n' for no.")
            
            if choice == 'n':
                print("\nThank you for using the HR Management System!")
                break


def get_valid_salary(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def main():
    hr_system = HRSystem()
    
    while True:
        try:
            num_employees = int(input("How many employees would you like to add? "))
            if num_employees > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    for i in range(num_employees):
        print(f"\nEnter details for Employee {i+1}:")
        name = input("Enter name: ")
        job_title = input("Enter job title: ")
        salary = get_valid_salary("Enter salary: $")
        hr_system.add_employee(name, job_title, salary)

    hr_system.display_all_employees()
    hr_system.process_raises()

if __name__ == "__main__":
    main()