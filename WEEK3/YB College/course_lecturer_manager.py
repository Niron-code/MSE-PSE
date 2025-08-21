from database import create_connection
import sqlite3

class CourseLecturer:
    def __init__(self, course_id, lecturer_id):
        self.course_id = course_id
        self.lecturer_id = lecturer_id

    @staticmethod
    def add_course_lecturer(course_id, lecturer_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO course_lecturer (course_id, lecturer_id) VALUES (?, ?)", (course_id, lecturer_id))
        conn.commit()
        conn.close()

    @staticmethod
    def view_course_lecturers():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT course_lecturer.id, course.name, lecturers.name
            FROM course_lecturer
            JOIN course ON course_lecturer.course_id = course.id
            JOIN lecturers ON course_lecturer.lecturer_id = lecturers.id
        ''')
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_course_lecturer(course_id, lecturer_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT course_lecturer.id, course.name, lecturers.name
            FROM course_lecturer
            JOIN course ON course_lecturer.course_id = course.id
            JOIN lecturers ON course_lecturer.lecturer_id = lecturers.id
            WHERE course_lecturer.course_id = ? AND course_lecturer.lecturer_id = ?
        ''', (course_id, lecturer_id))
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete_course_lecturer(course_lecturer_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM course_lecturer WHERE id = ?", (course_lecturer_id,))
        conn.commit()
        conn.close()