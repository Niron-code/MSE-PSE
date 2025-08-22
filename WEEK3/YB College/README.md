# YB College Management System

This project is a simple college management system built with Python and SQLite. It manages students, courses, lecturers, enrollments, and course-lecturer assignments.

## Features
 Menu navigation for easy access to all features
 Add, view, search, delete, and update students, courses, and lecturers
 Enroll students in courses
 Assign lecturers to courses
 View enrollments with student names and course names
 View Courese and Lecturer relationship
 Name and email validation for students and lecturers to ensure correct data entry

## Structure
- `database.py`: Handles database connection and table creation
- `student_manager.py`: Manages student operations
- `course_manager.py`: Manages course operations
- `lecturer_manager.py`: Manages lecturer operations
- `enrollment_manager.py`: Manages enrollments (student-course relationships)
- `course_lecturer_manager.py`: Manages course-lecturer assignments
- `menu.py`: Provides the user interface and navigation for the application
- `main.py`: Main entry point for running the application
- `Documentation/`: Contains ER diagrams and documentation
- `utility.py`: Provides validation functions for names and emails to ensure data integrity when adding or updating students and lecturers.


## Database Schema
See `Documentation/ER_Diagram.png` for the entity-relationship diagram.

## Getting Started
1. Ensure you have Python 3 installed.
2. Run `main.py` to start the application.
3. The database will be created automatically if it does not exist.

## License
This project is for educational purposes.
