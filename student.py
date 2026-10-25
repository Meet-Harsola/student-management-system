class Student:
    def __init__(self, student_id, name, age, course, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.email = email

    def display_details(self):
        print("\n ----- Student Details -----")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
        print(f"Email      : {self.email}")

    def update_email(self, new_email):
        self.email = new_email
        print("Email updated successfully!")

