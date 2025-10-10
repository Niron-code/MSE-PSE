from dataclasses import dataclass
from typing import List
try:
    # when used as a package
    from .database import DatabaseManager
except Exception:
    # when tests import module as top-level (sys.path modified)
    from database import DatabaseManager


ALLOWED_TYPES = {"Transport", "Rent", "Bills", "Grocery"}


@dataclass
class Expense:
    description: str
    amount: float
    type: str


class PersonalExpenseTracker:
    def __init__(self, db_path: str = ":memory:"):
        self.db = DatabaseManager(db_path)
        self.db.initialize()

    def add_expense(self, description: str, amount: float, type_: str) -> int:
        """Add an expense and return its id.

        Raises ValueError for invalid input.
        """
        if not description or not isinstance(description, str):
            raise ValueError("Description must be a non-empty string")
        if not isinstance(amount, (int, float)):
            # try to coerce numeric-like strings to float
            try:
                amount = float(amount)
            except (TypeError, ValueError) as e:
                raise ValueError("Amount must be a number") from e
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        if type_ not in ALLOWED_TYPES:
            raise ValueError(f"Type must be one of: {', '.join(sorted(ALLOWED_TYPES))}")

        return self.db.add_expense(description, amount, type_)

    def list_expenses(self) -> List[Expense]:
        rows = self.db.get_all_expenses()
        return [Expense(description=r[1], amount=r[2], type=r[3]) for r in rows]

    def total_expense(self) -> float:
        rows = self.db.get_all_expenses()
        total = sum(r[2] for r in rows)
        return float(total)

    def clear_expenses(self):
        self.db.clear()

    def close(self):
        self.db.close()
