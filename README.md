# 🎓 Student Management System

A console-based **Student Management System built using Python and SQLite**. This project demonstrates object-oriented programming, database management, CRUD operations, input validation, exception handling, and automated testing using Python's `unittest` framework.

---

## 📌 Project Overview

The Student Management System is a command-line application that allows users to manage student records efficiently.

Users can add new students, view all registered students, search for a student by ID, update student information, and delete records. Student information is stored in an SQLite database, ensuring that records persist even after the application is closed.

This project was developed to strengthen Python programming, database management, and software testing skills through practical implementation.

## ✨ Features

- **Add Students:** Register students with an ID, name, age, course, and email address.
- **View All Students:** Display all registered student records.
- **Search Students:** Retrieve student details using a student ID.
- **Update Student Details:** Modify existing student information.
- **Delete Students:** Remove student records with confirmation.
- **Input Validation:** Reject invalid IDs, ages, empty names, empty courses, and invalid email addresses.
- **Duplicate Prevention:** Prevent duplicate student IDs and email addresses.
- **Persistent Storage:** Store student records in an SQLite database.
- **Exception Handling:** Handle database errors gracefully.
- **Automated Testing:** Verify application functionality using Python's built-in `unittest` framework.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Application development |
| SQLite | Database management and persistent storage |
| `sqlite3` | Python interface for SQLite |
| Object-Oriented Programming | Organizing application logic |
| `unittest` | Automated testing |
| Visual Studio Code | Development environment |
| Git and GitHub | Version control and project hosting |

## 📂 Project Structure

```text
student-management-system/
│
├── main.py
├── student.py
├── database.py
├── student_manager.py
├── README.md
├── .gitignore
│
└── tests/
    └── test_student_manager.py
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Runs the application and displays the interactive menu. |
| `student.py` | Defines the `Student` class and its attributes. |
| `database.py` | Initializes the SQLite database and performs database operations. |
| `student_manager.py` | Handles business logic, input validation, and error handling. |
| `tests/test_student_manager.py` | Contains automated unit tests. |
| `README.md` | Documents the project, features, and setup instructions. |
| `.gitignore` | Specifies files and directories that Git should ignore. |

**Note:** The `students.db` database file is created when the application initializes the database. It is not included in the repository structure because local database files should generally be excluded from version control.

## ⚙️ Prerequisites

Before running the application, ensure that you have:

- Python 3 installed.
- Visual Studio Code or another code editor.
- A terminal for executing Python commands.
- Git installed if you want to upload the project to GitHub.

The project uses Python's standard library, so no additional packages are required.

### Verify Python Installation

```bash
python3 --version
```

### Verify SQLite Availability

```bash
python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
```

## 🚀 Installation and Setup

### Step 1: Get the Project

If you have uploaded the project to GitHub, clone your repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

Navigate to the project directory:

```bash
cd student-management-system
```

Alternatively, open your existing project folder directly in Visual Studio Code.

### Step 2: Run the Application

From the project root directory, execute:

```bash
python3 main.py
```

The application initializes the database if necessary and displays the interactive menu.

## 🖥️ Application Usage

When you run the application, an interactive menu allows you to select an operation.

### Main Menu

```text
===== Student Management System =====

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter your choice:
```

### Available Operations

**1. Add Student**

Enter the student's ID, name, age, course, and email address. The application validates the input before saving the record.

**2. View All Students**

Displays the student records stored in the database.

**3. Search Student**

Searches for a student using their unique student ID.

**4. Update Student**

Updates the details of an existing student.

**5. Delete Student**

Deletes a student record after confirmation.

**6. Exit**

Closes the application.

## 🗄️ Database Design

The application uses SQLite to store student records in a table named `students`.

### Students Table

| Column | Data Type | Constraint |
|---|---|---|
| `student_id` | INTEGER | Primary key |
| `name` | TEXT | Required |
| `age` | INTEGER | Required; must be greater than zero |
| `course` | TEXT | Required |
| `email` | TEXT | Required and unique |

### Database Highlights

- Student records are stored persistently.
- Primary key constraints prevent duplicate student IDs.
- Unique constraints prevent duplicate email addresses.
- Parameterized SQL queries help protect against SQL injection.
- Database connections are closed after operations.

## 🧪 Automated Testing

The project uses Python's built-in `unittest` framework to test the main application features.

### Run the Test Suite

From the project root directory, execute:

```bash
python3 -m unittest discover -s tests -v
```

### Test Coverage

The current test suite contains 13 test cases covering:

- Valid student registration.
- Invalid student IDs.
- Invalid ages.
- Empty student names.
- Empty course names.
- Invalid email addresses.
- Duplicate student IDs.
- Duplicate email addresses.
- Searching for an existing student.
- Searching for a nonexistent student.
- Updating student details.
- Deleting an existing student.
- Deleting a nonexistent student.

### Test Results

All 13 test cases have passed during development.

Expected test summary:

```text
Ran 13 tests in 0.015s

OK
```

The actual execution time may vary depending on your system.

**Testing note:** The test suite uses a separate temporary database to prevent test operations from modifying your regular student records.

## 🔒 Input Validation and Error Handling

The application validates user input before performing database operations.

Examples include:

- Student IDs must be positive integers.
- Ages must be valid integers within the accepted range.
- Student names cannot be empty.
- Course names cannot be empty.
- Email addresses must satisfy the application's basic email-validation rules.
- Duplicate student IDs and email addresses are rejected.
- Database errors are handled with appropriate error messages.

## 🔮 Future Enhancements

Possible improvements for future versions include:

- Develop a graphical user interface using Tkinter.
- Add student sorting and filtering.
- Implement pagination for large datasets.
- Export student records to CSV or Excel.
- Generate course-wise student reports.
- Add role-based authentication and authorization.
- Expand automated testing to cover more edge cases.
- Introduce structured logging.
- Develop a web-based version using Flask or Django.

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

- Python programming and object-oriented design.
- Modular application development.
- SQLite database design and CRUD operations.
- Input validation and exception handling.
- Automated testing using `unittest`.
- Debugging and resolving software defects.
- Organizing a project for version control and GitHub.

## 👨‍💻 Author

**Student Management System — Python Project**

Developed as a hands-on project to practice Python programming, database management, and software testing.

---

*This project is intended for educational and demonstration purposes.*