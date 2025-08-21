from database import create_connection
import sqlite3

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    @staticmethod
    def add_course(name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO course (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

    @staticmethod
    def view_courses():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_course(name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete_course(course_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM course WHERE id = ?", (course_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_course(course_id, name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE course SET name = ? WHERE id = ?", (name, course_id))
        conn.commit()
        conn.close()
