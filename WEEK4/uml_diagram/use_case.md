## Entity Relationship Description

The **YB College database** is designed to manage and organize essential information about students, lecturers, courses, and enrollments. It records:
- Student details
- Lecturer profiles
- Course information
- Which students are enrolled in which courses

### Entities
- **STUDENT**: Each student has a unique ID, name, profile, and contact info.
- **LECTURER**: Each lecturer has a unique ID, name, profile, and contact info.
- **COURSE**: Each course has a unique ID, a name, and is taught by many lecturers (`lecturer_id` is a foreign key).
- **ENROLLMENT**: Links students to courses, recording each enrollment with its own ID, and foreign keys for student and course.
- **LECTURER_COURSE**: Represents the many-to-many relationship between lecturers and courses. Each record contains a unique ID, a `lecturer_id` (FK), and a `course_id` (FK).

---
## Use Cases

### Actors
- **ADMIN**
- **Lecturer**
- **Student**

### ADMIN
- Managing student record
- Managing lecturer record
- Enrolling student to course
- Assigning lecturer to the course

### Lecturer
- Update lecturer details
- Managing the course

### Student
- Update student details
- Enrolling to course