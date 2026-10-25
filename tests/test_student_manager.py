import unittest
import tempfile
from pathlib import Path

import database
from student_manager import StudentManager


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        """
        Create a separate temporary database before each test.
        """
        self.temp_directory = tempfile.TemporaryDirectory()

        self.original_database_name = database.DATABASE_NAME

        database.DATABASE_NAME = (
            Path(self.temp_directory.name) / "test_students.db"
        )

        database.initialize_database()

        self.manager = StudentManager()

    def tearDown(self):
        """
        Restore the original database path and clean up.
        """
        database.DATABASE_NAME = self.original_database_name
        self.temp_directory.cleanup()

    def test_add_valid_student(self):
        success, message = self.manager.add_student(
            101,
            "Rahul Sharma",
            22,
            "Computer Science",
            "rahul@example.com"
        )

        self.assertTrue(success)
        self.assertEqual(
            message,
            "Student added successfully."
        )

        student = self.manager.get_student(101)

        self.assertIsNotNone(student)
        self.assertEqual(student[1], "Rahul Sharma")

    def test_invalid_student_id(self):
        success, message = self.manager.add_student(
            "abc",
            "Rahul Sharma",
            22,
            "Computer Science",
            "rahul@example.com"
        )

        self.assertFalse(success)
        self.assertEqual(
            message,
            "Student ID must be a positive integer."
        )

    def test_invalid_age(self):
        success, message = self.manager.add_student(
            102,
            "Priya Sharma",
            "abc",
            "Computer Science",
            "priya@example.com"
        )

        self.assertFalse(success)

    def test_empty_name(self):
        success, message = self.manager.add_student(
            103,
            "",
            21,
            "Computer Science",
            "student103@example.com"
        )

        self.assertFalse(success)

    def test_empty_course(self):
        success, message = self.manager.add_student(
            104,
            "Amit Patel",
            21,
            "",
            "amit@example.com"
        )

        self.assertFalse(success)

    def test_invalid_email(self):
        success, message = self.manager.add_student(
            105,
            "Neha Patel",
            21,
            "Computer Science",
            "invalid-email"
        )

        self.assertFalse(success)

    def test_duplicate_student_id(self):
        self.manager.add_student(
            106,
            "Student One",
            21,
            "Computer Science",
            "one@example.com"
        )

        success, message = self.manager.add_student(
            106,
            "Student Two",
            22,
            "Information Technology",
            "two@example.com"
        )

        self.assertFalse(success)
        self.assertEqual(
            message,
            "Student ID or email already exists."
        )

    def test_duplicate_email(self):
        self.manager.add_student(
            107,
            "Student One",
            21,
            "Computer Science",
            "shared@example.com"
        )

        success, message = self.manager.add_student(
            108,
            "Student Two",
            22,
            "Information Technology",
            "shared@example.com"
        )

        self.assertFalse(success)
        self.assertEqual(
            message,
            "Student ID or email already exists."
        )

    def test_search_existing_student(self):
        self.manager.add_student(
            109,
            "Karan Mehta",
            23,
            "Computer Science",
            "karan@example.com"
        )

        student = self.manager.get_student(109)

        self.assertIsNotNone(student)
        self.assertEqual(student[1], "Karan Mehta")

    def test_search_nonexistent_student(self):
        student = self.manager.get_student(9999)

        self.assertIsNone(student)

    def test_update_student(self):
        self.manager.add_student(
            110,
            "Old Name",
            22,
            "Computer Science",
            "old@example.com"
        )

        success, message = self.manager.update_student(
            110,
            "New Name",
            23,
            "Information Technology",
            "new@example.com"
        )

        self.assertTrue(success)

        student = self.manager.get_student(110)

        self.assertIsNotNone(student)
        self.assertEqual(student[1], "New Name")
        self.assertEqual(student[2], 23)
        self.assertEqual(student[3], "Information Technology")
        self.assertEqual(student[4], "new@example.com")

    def test_delete_existing_student(self):
        self.manager.add_student(
            111,
            "Delete Me",
            22,
            "Computer Science",
            "delete@example.com"
        )

        success, message = self.manager.delete_student(111)

        self.assertTrue(success)
        self.assertIsNone(self.manager.get_student(111))

    def test_delete_nonexistent_student(self):
        success, message = self.manager.delete_student(9999)

        self.assertFalse(success)


if __name__ == "__main__":
    unittest.main()