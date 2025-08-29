# Base/Parent class - Contains common attributes for all persons
class Person:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}\nAddress: {self.address}\nAge: {self.age}"
