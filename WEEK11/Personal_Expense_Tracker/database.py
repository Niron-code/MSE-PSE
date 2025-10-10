import sqlite3
from typing import Optional, List, Tuple


class DatabaseManager:
    """Simple sqlite3 wrapper for the expense tracker."""

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None

    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def initialize(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                type TEXT NOT NULL
            )
            """
        )
        conn.commit()

    def add_expense(self, description: str, amount: float, type_: str) -> int:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO expenses (description, amount, type) VALUES (?, ?, ?)",
            (description, amount, type_),
        )
        conn.commit()
        return cur.lastrowid

    def get_all_expenses(self) -> List[Tuple[int, str, float, str]]:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT id, description, amount, type FROM expenses")
        rows = cur.fetchall()
        return [(r[0], r[1], r[2], r[3]) for r in rows]

    def clear(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM expenses")
        conn.commit()
