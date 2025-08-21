from database import create_connection
import sqlite3

class Student:
    def __init__(self, student_id, name, email, profile):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.profile = profile

    @staticmethod
    def add_student(name, email, profile):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, email, profile) VALUES (?, ?, ?)", (name, email, profile))
        conn.commit()
        conn.close()

    @staticmethod
    def view_students():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_student(name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete_student(student_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_student(student_id, name, email, profile):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name = ?, email = ?, profile = ? WHERE id = ?", (name, email, profile, student_id))
        conn.commit()
        conn.close()
