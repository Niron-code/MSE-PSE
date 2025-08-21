from database import create_connection
import sqlite3

class Lecturer:
    def __init__(self, lecturer_id, name, email, profile):
        self.lecturer_id = lecturer_id
        self.name = name
        self.email = email
        self.profile = profile

    @staticmethod
    def add_lecturer(name, email, profile):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO lecturers (name, email, profile) VALUES (?, ?, ?)", (name, email, profile))
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

    @staticmethod
    def update_lecturer(lecturer_id, name, email, profile):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE lecturers SET name = ?, email = ?, profile = ? WHERE id = ?", (name, email, profile, lecturer_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_lecturer(lecturer_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lecturers WHERE id = ?", (lecturer_id,))
        row = cursor.fetchone()
        conn.close()
        return row
