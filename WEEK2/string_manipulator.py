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
character = name.find_character('x')
print("Character position is : ",character)  # Output: 1

# Call the find_length and convert_to_uppercase methods
length = name.find_length()
print("Length of the word is : ",length)  # Output: 7

# Call the convert_to_uppercase method
uppercase_text = name.convert_to_uppercase()
print("Upper case word is : ",uppercase_text)  # Output: EXAMPLE
