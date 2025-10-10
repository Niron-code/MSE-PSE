import contextlib
import unittest
import os
import sys

# Ensure local package path is first so tests can import the module when run directly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from personal_expense_tracker import PersonalExpenseTracker, Expense


class TestPersonalExpenseTracker(unittest.TestCase):
    def setUp(self):
        # use an on-disk temporary DB so multiple connections behave consistently
        self.db_path = 'test_expenses.db'
        # ensure any leftover test DB is removed
        try:
            os.remove(self.db_path)
        except OSError:
            pass
        # create tracker after cleanup
        self.tracker = PersonalExpenseTracker(db_path=self.db_path)

    def tearDown(self):
        self.tracker.close()
        try:
            os.remove(self.db_path)
        except OSError:
            pass

    def test_add_and_total_single(self):
        self.tracker.add_expense('Coffee', 3.5, 'Grocery')
        total = self.tracker.total_expense()
        self.assertAlmostEqual(total, 3.5)

    def test_add_multiple_and_total(self):
        self.tracker.add_expense('Lunch', 10, 'Transport')
        self.tracker.add_expense('Book', 15.25, 'Bills')
        self.tracker.add_expense('Snack', 2.75, 'Grocery')
        total = self.tracker.total_expense()
        self.assertAlmostEqual(total, 28.0)

    def test_list_expenses(self):
        id1 = self.tracker.add_expense('Item1', 5, 'Transport')
        id2 = self.tracker.add_expense('Item2', 7, 'Rent')
        items = self.tracker.list_expenses()
        self.assertEqual(len(items), 2)
        # items are Expense dataclasses
        self.assertEqual(items[0].description, 'Item1')
        self.assertEqual(items[1].description, 'Item2')

    def test_invalid_description(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense('', 5, 'Grocery')

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense('Bad', 'not-a-number', 'Bills')

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            self.tracker.add_expense('Refund', -10, 'Rent')


if __name__ == '__main__':
    unittest.main()
