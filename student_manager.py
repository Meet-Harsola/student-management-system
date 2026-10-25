import sqlite3

from student import Student
from database import ( add_student as db_add_student, get_all_students as db_get_all_students, get_student_by_id as db_get_student_by_id, update_student as db_update_student, delete_student as db_delete_student)
import re

def validate_student_id(student_id):
    """Validate that the student ID is a positive integer."""

    try:
        student_id = int(student_id)
        return student_id > 0
    except (ValueError, TypeError):
        return False
    
def validate_age(age):
    """Validate that age is a positive integer."""

    try:
        age = int(age)
        return 1 <= age <= 120
    except (ValueError, TypeError):
        return False
    
def validate_name(name):
    """Validate that the course is not empty."""

    return isinstance(name, str) and bool(name.strip())

def validate_course(course):
    """Validate that the course is not empty."""

    return isinstance(course, str) and bool(course.strip())

def validate_email(email):
    """Perform basic email format Valdation"""

    if not isinstance(email, str):
        return False
    
    email = email.strip()


    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(re.fullmatch(pattern, email))




class StudentManager:

    def add_student(self, student_id, name, age, course, email):
        """Validate and register a student."""

        if not validate_student_id(student_id):
            return False, "Student ID must be a positive integer."
        
        if not validate_name(name):
            return False, "Student name cannot be empty."
        
        if not validate_age(age):
            return False, "Age must be an integer between 1 and 120."

        if not validate_course(course):
            return False, "Course can not be Empty."
        
        if not validate_email(email):
            return False, "Please enter a valid email address."
        

        student_id = int(student_id)
        age = int(age)
        name = name.strip()
        course = course.strip()
        email = email.strip()

        student = Student(
            student_id,
            name,
            age,
            course,
            email
        )

        try:
            db_add_student(student)

            return True, "Student added successfully."
        
        except sqlite3.IntegrityError as error:
            print("INTEGRITY ERROR:", repr(error))
            return False, "Student ID or email already exists."

        except sqlite3.Error as error:
            print("DATABASE ERROR TYPE:", type(error).__name__)
            print("DATABASE ERROR DETAILS:", repr(error))
            return False, "A Database error occurred while adding the student."
        
    def get_all_students(self):
        """Return all registered Students."""
        return db_get_all_students()
        
    
    def get_student(self, student_id):
        """Find a student by ID."""

        if not validate_student_id(student_id):
            return None
        
        try:

            student_id = int (student_id)
            
            return db_get_student_by_id(student_id)
        
        except sqlite3.Error:
            return None
        
    def update_student(self, student_id, name, age, course, email):
        """Validate and update an existing student."""
        

        if not validate_student_id(student_id):
            return False, "Student ID must be a positive integer."
        
        if not validate_name(name):
            return False, "Student name cannot be empty."
        
        if not validate_age(age):
            return False, "Age must be an integer between 1 and 120."

        if not validate_course(course):
            return False, "Course can not be Empty."
        
        if not validate_email(email):
            return False, "Please enter a valid email address."

        student_id = int(student_id)
        age = int(age)
        name = name.strip()
        course = course.strip()
        email = email.strip()        
        
        try:
            
            if self.get_student(student_id) is None:
                return False, "Student not found."
            
            updated = db_update_student(
                student_id,
                name,
                age,
                course,
                email
            )


            if updated:
                return True, "Student updated Successfully."
            
            return False, "Student not found"
        
        except sqlite3.Error:
            return False, "A Database error occured while updating the student."
        
        except sqlite3.IntegrityError:
            return False,"That email address is already registered."
        
    def delete_student(self, student_id):
        """Delete a student if the ID is valid."""

        if not validate_student_id(student_id):
            return False, "Student Id must be a positive Intgere."

        try:
            student_id = int(student_id)
            
            deleted = db_delete_student(student_id)

            if deleted:
                return True, "Student record deleted Successfully."
            
            return False, "Student not found."
        
        except sqlite3.Error:
            return False, "A Database error occured while deleting the student."
        

