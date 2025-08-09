class StringManipulator:
    def __init__(self, text):
        self.text = text
    
    def find_character(self, char):
        return self.text.find(char)
    
    def find_length(self):
        return len(self.text)
    
    def convert_to_uppercase(self):
        return self.text.upper()

# Create an instance of the StringManipulator class
name = StringManipulator("example")

# Call the find_character method on the object
result = name.find_character('x')
print(result)  # Output: 1

length = name.find_length()
print(length)  # Output: 7

uppercase_text = name.convert_to_uppercase()
print(uppercase_text)  # Output: EXAMPLE
