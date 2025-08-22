from database import create_connection

class Enrollment:
    def __init__(self, enrollment_id, student_id, course_id):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_id = course_id

    @staticmethod
    def add_enrollment(student_id, course_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO enrollment (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        conn.commit()
        conn.close()

    @staticmethod
    def view_enrollments():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT enrollment.id, students.name, course.name
            FROM enrollment
            JOIN students ON enrollment.student_id = students.id
            JOIN course ON enrollment.course_id = course.id
        ''')
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_enrollment(student_id, course_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT enrollment.id, students.name, course.name
            FROM enrollment
            JOIN students ON enrollment.student_id = students.id
            JOIN course ON enrollment.course_id = course.id
            WHERE enrollment.student_id = ? AND enrollment.course_id = ?
        ''', (student_id, course_id))
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def delete_enrollment(enrollment_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM enrollment WHERE id = ?", (enrollment_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_enrollment(enrollment_id, student_id, course_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE enrollment SET student_id = ?, course_id = ? WHERE id = ?", (student_id, course_id, enrollment_id))
        conn.commit()
        conn.close()
