import re
class Utility:
    @staticmethod
    def namevalidator(name):
        # name should be alphabetic, can include spaces
        if not name.replace(" ", "").isalpha():
            print("Invalid name. Name must be alphabetic.")
            return False
        return True

    @staticmethod
    def emailvalidator(email): #regex
        # Simple email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            print(f"Error: '{email}' is not a valid email address. Please enter a valid email (e.g., user@example.com).")
            return False
        return True