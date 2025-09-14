"""
Magazine Class
-------------
This class represents a magazine in the library management system.

OOP Concepts Demonstrated:
1. Inheritance:
   - Magazine inherits from LibraryItem, reusing its attributes and methods.
2. Encapsulation:
   - Adds a protected attribute _issue_frequency with a getter method.
3. Polymorphism:
   - Overrides the display_details method to provide magazine-specific output.

Usage:
    Create a Magazine object with title, author, and issue frequency, then use display_details to show its information.
"""

from LibraryItem import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, issue_frequency):
        """Initializes a Magazine with title, author, and issue frequency."""
        super().__init__(title, author)
        self._issue_frequency = issue_frequency

    def get_issue_frequency(self):
        """Returns the issue frequency of the magazine."""
        return self._issue_frequency

    def display_details(self):
        """Displays the details of the magazine item."""
        print(f"[Magazine] Title: {self.get_title()}, Author: {self.get_author()}, Issue Frequency: {self._issue_frequency}")