"""
Book Class
----------
This class represents a book in the library management system.

OOP Concepts Demonstrated:
1. Inheritance:
   - Book inherits from LibraryItem, reusing its attributes and methods.
2. Polymorphism:
   - Overrides the display_details method to provide book-specific output.

Usage:
    Create a Book object with a title and author, then use display_details to show its information.
"""

from LibraryItem import LibraryItem

class Book(LibraryItem):
    def display_details(self):
        """Displays the details of the book item."""
        print(f"[Book] Title: {self.get_title()}, Author: {self.get_author()}")