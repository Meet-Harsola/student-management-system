import sqlite3
from pathlib import Path

DATABASE_NAME = Path(__file__).resolve().parent / "students.db"


def get_connection():

    """Create and return a connection to the SQLite database."""
    connection = sqlite3.connect(DATABASE_NAME)
    return connection

def initialize_database():
    """Create the student table if it does not exist."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                       student_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       age INTEGER NOT NULL CHECK (age > 0),
                       course TEXT NOT NULL,
                       email TEXT NOT NULL UNIQUE
                )
        """)

        connection.commit()
        #print("Database initialized successfully!")

    finally:
        connection.close()


def add_student(student):
    """Insert a student object into the database."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO students
            (student_id, name, age, course, email)
            VALUES (?, ?, ?, ?, ?)
        """, (
            student.student_id,
            student.name,
            student.age,
            student.course,
            student.email
        ))

        connection.commit()

    finally:
        connection.close()


def get_all_students():
    """Retrive all student records from Database."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT student_id, name, age, course, email
            FROM students
            ORDER BY student_id
        """)

        students = cursor.fetchall()
        return students
    
    finally:
        connection.close()

def get_student_by_id(student_id):
    """Retrives a student using their ID"""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT student_id, name, age, course, email
            FROM students
            WHERE student_id = ?
            """,
            (student_id,)
        )

        return cursor.fetchone()
    
    finally:
        connection.close()

def update_student(student_id, name, age, course, email):
    """Update an existing student's information."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE students SET name = ?, age = ?, course = ?, email = ?
            WHERE student_id = ?
            """,
            (name, age, course, email, student_id)
        )

        connection.commit()

        return cursor.rowcount > 0
    
    finally:
        connection.close()

def delete_student(student_id):
    "Delete a student using their ID."

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM students
            WHERE student_id = ?
            """,
            (student_id,)
        )

        connection.commit()

        return cursor.rowcount > 0
    
    finally:
        connection.close()

    

