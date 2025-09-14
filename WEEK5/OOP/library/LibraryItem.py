"""
LibraryItem Base Class
---------------------
This class demonstrates key Object-Oriented Programming (OOP) concepts:

1. Encapsulation:
   - Attributes `_title` and `_author` are protected (single underscore), restricting direct access from outside the class.
   - Getter methods (`get_title`, `get_author`) provide controlled access to these attributes.

2. Inheritance:
   - Other classes (e.g., Book, Magazine) inherit from LibraryItem, reusing its attributes and methods.

3. Polymorphism:
   - Subclasses can override methods (e.g., display_details) to provide specific behavior.

Usage:
    Subclass LibraryItem to create specific item types (Book, Magazine) and override methods as needed.
"""

class LibraryItem:
    def __init__(self, title, author):
        # Protected attributes for encapsulation
        self._title = title
        self._author = author

    def get_title(self):
        """Returns the title of the library item."""
        return self._title

    def get_author(self):
        """Returns the author of the library item."""
        return self._author

    def display_details(self):
        """Displays the details of the library item."""
        print(f"Title: {self._title}, Author: {self._author}")