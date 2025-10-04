
"""Text analysis module for analyzing strings and lists of strings."""
from typing import Union, List


class TextAnalyzer:
    """Text analysis tool for strings and lists of strings."""

    def __init__(self, data: Union[str, List[str]]):
        self.data = data
        self._validate_data()  # Check data type on initialization

    def _validate_data(self) -> None:
        """Ensure data is string or list of strings."""
        if not isinstance(self.data, (str, list)):
            raise TypeError("Data must be a string or list of strings")
        if isinstance(self.data, list):
            for item in self.data:
                if not isinstance(item, str):
                    raise TypeError("All list items must be strings")

    def calculate_total_length(self) -> int:
        """Return total character count."""
        if isinstance(self.data, str):
            return len(self.data)
        return sum(len(item) for item in self.data)  # Sum lengths for list

    def count_uppercase_characters(self) -> int:
        """Count uppercase letters."""
        if isinstance(self.data, str):
            return len([char for char in self.data if char.isupper()])
        return sum(len([char for char in item if char.isupper()]) for item in self.data)

    def count_digits(self) -> int:
        """Count numeric characters (0-9)."""
        if isinstance(self.data, str):
            return len([char for char in self.data if char.isdigit()])
        return sum(len([char for char in item if char.isdigit()]) for item in self.data)

    def count_special_characters(self) -> int:
        """Count non-alphanumeric, non-whitespace characters."""
        if isinstance(self.data, str):
            return len([char for char in self.data if not char.isalnum() and not char.isspace()])
        return sum(len([char for char in item if not char.isalnum() and not char.isspace()])
                  for item in self.data)

    def get_data_type(self) -> str:
        """Return data type name."""
        return type(self.data).__name__

    def analyze(self) -> dict:
        """Return all analysis results in a dictionary."""
        return {
            'data_type': self.get_data_type(),
            'data': self.data,
            'total_length': self.calculate_total_length(),
            'uppercase_count': self.count_uppercase_characters(),
            'digit_count': self.count_digits(),
            'special_char_count': self.count_special_characters()
        }

    def display_results(self) -> None:
        """Print formatted analysis results."""
        analysis_results = self.analyze()
        print("\n" + "="*60)
        print("TEXT ANALYSIS RESULTS")
        print("="*60)
        print(f"Data Type: {analysis_results['data_type']}")
        print(f"Data: {analysis_results['data']}")
        print("-" * 60)
        print("CHARACTER ANALYSIS:")
        print(f"  Total Length: {analysis_results['total_length']}")
        print(f"  Uppercase Characters: {analysis_results['uppercase_count']}")
        print(f"  Digit Characters: {analysis_results['digit_count']}")
        print(f"  Special Characters: {analysis_results['special_char_count']}")
        print("="*60)


# Demo examples
if __name__ == "__main__":
    # String with mixed characters
    print("=== DEMO 1: String Analysis ===")
    analyzer1 = TextAnalyzer("Hello WORLD! This is a TEST String with 123 digits!")
    analyzer1.display_results()

    # List of strings
    print("\n=== DEMO 2: List Analysis ===")
    analyzer2 = TextAnalyzer(["Python@2024", "PROGRAMMING!", "Test#123", "DATA$"])
    analyzer2.display_results()

    # Complex text with email, phone, price
    print("\n=== DEMO 3: Complex Text Analysis ===")
    COMPLEX_TEXT = "Email: user@example.com | Phone: +1-555-123-4567 | Price: $99.99"
    analyzer3 = TextAnalyzer(COMPLEX_TEXT)
    analyzer3.display_results()

    # Access results programmatically
    print("\n=== DEMO 4: Programmatic Analysis ===")
    test_data = ["Hello123!", "WORLD@2024", "Python#Code$"]
    analyzer4 = TextAnalyzer(test_data)
    analysis_data = analyzer4.analyze()  # Get raw results
    print(f"Analysis Results: {analysis_data}")
