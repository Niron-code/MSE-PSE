from database import create_connection
import sqlite3

class Lecturer:
    def __init__(self, lecturer_id, name, email):
        self.lecturer_id = lecturer_id
        self.name = name
        self.email = email

    @staticmethod
    def add_lecturer(name, email):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO lecturers (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
        except sqlite3.IntegrityError:
            pass
        conn.close()

    @staticmethod
    def view_lecturers():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lecturers")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_lecturer(name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lecturers WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete_lecturer(lecturer_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM lecturers WHERE id = ?", (lecturer_id,))
        conn.commit()
        conn.close()
