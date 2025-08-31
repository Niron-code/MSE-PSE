"""
Library Management System
------------------------
This module defines a simple library management system using OOP principles.
It includes classes for Library, Book, and Magazine, demonstrating inheritance and encapsulation.

Classes:
    Library: Manages a collection of library items (books and magazines).
    Book: Represents a book item (see Book.py).
    Magazine: Represents a magazine item (see Magazine.py).

Example usage is provided in the main() function.
"""

from Book import Book
from Magazine import Magazine

class Library:
    """
    Manages a collection of library items (books and magazines).
    Methods:
        add_item(item): Adds a LibraryItem to the collection.
        remove_item(item): Removes a LibraryItem from the collection.
        display_all_items(): Displays details of all items in the library.
    """
    def __init__(self):
        """Initializes the library with an empty list of items."""
        self._items = []

    def add_item(self, item):
        """Adds a LibraryItem (Book or Magazine) to the library."""
        self._items.append(item)
        print(f"Item added: {item.get_title()}")

    def remove_item(self, item):
        """Removes a LibraryItem from the library if it exists."""
        if item in self._items:
            self._items.remove(item)
            print(f"Item removed: {item.get_title()}")
        else:
            print("Item not found in library.")

    def display_all_items(self):
        """Displays details of all items currently in the library."""
        print("Library Items:")
        for item in self._items:
            item.display_details()

def main():
    """
    Example usage of the Library management system.
    Adds books and magazines, removes some items, and displays the library contents.
    """
    # Add Python programming books
    book1 = Book("Learning Python", "Mark Lutz")
    book2 = Book("Python Crash Course", "Eric Matthes")
    
    # Add Python-related magazines
    magazine1 = Magazine("Python Software Foundation Newsletter", "Python Community", "Monthly")
    magazine2 = Magazine("Linux Journal (Python section)", "Various", "Monthly")

    # Create library instance
    library = Library()

    # Add items to library
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine1)
    library.add_item(magazine2)

    # Remove items from library
    library.remove_item(book1)
    library.remove_item(magazine1)

    # Display all items
    library.display_all_items()

if __name__ == "__main__":
    main()