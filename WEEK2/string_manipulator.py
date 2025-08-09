class StringManipulator:
    # __init__ method removed
    
    def find_character(self, text, char):
        return text.find(char)
    
    def find_length(self, text):
        return len(text)
    
    def convert_to_uppercase(self, text):
        return text.upper()

# Use the StringManipulator class without __init__
manipulator = StringManipulator()
text = "example"

# Call the find_character method
character = manipulator.find_character(text, 'x')
print("Character position is : ", character)  # Output: 1

# Call the find_length and convert_to_uppercase methods
length = manipulator.find_length(text)
print("Length of the word is : ", length)  # Output: 7

# Call the convert_to_uppercase method
uppercase_text = manipulator.convert_to_uppercase(text)
print("Upper case word is : ", uppercase_text)  # Output: EXAMPLE
