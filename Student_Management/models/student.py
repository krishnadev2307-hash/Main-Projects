"""Design of student class, creates and initializes a student object
Note: Student id is automatically created in the database."""
class Student:
    def __init__ (self,student_name: str,student_age: int,branch_id: int,semester: int,marks: dict,
                  attendance: float,phone_number: str,email: str) -> None:
        self.student_name = student_name
        self.student_age = student_age
        self.branch_id = branch_id
        self.semester = semester
        self.marks = marks
        self.phone_number = phone_number
        self.attendance = attendance
        self.email = email