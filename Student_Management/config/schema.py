"""
So we are creating tables before we execute main, so
Database : StudentManagement
Tables:
->Branches: Contains branch_id and branch_name
->Subjects: Contains subject_id and subject_name
->Students: Contains the basic information of a student: Name,Age,Branch_id,Semester,Attendance,Phone_number,Email
->Marks: Contains the subject_id,student_id,marks
Note: This is a setup script which only runs once and this is already executed.
"""
from Student_Management.config.database import Database
from Student_Management.config.Branches import create_branches
from Student_Management.config.Subjects import create_subjects
DATABASE = Database()
connection = DATABASE.connect()
create_branches()
create_subjects()
cursor = connection.cursor()
query1= '''Create table branches(Branch_id int primary key,
                        Branch_name varchar(30) not null unique);'''
cursor.execute(query1)
connection.commit()
query2 = '''Create table subjects (subject_id int primary key,
                    subject_name varchar(30) not null unique);'''
cursor.execute(query2)
connection.commit()
query3 = '''Create table students (student_id int primary key auto_increment,
                student_name varchar(30) not null,
                student_age int not null,
                branch_id int not null,
                semester int not null,
                attendance float not null,
                phone_number varchar(30) not null,
                email varchar(30) not null,
                foreign key(branch_id) references branches(Branch_id));'''
cursor.execute(query3)
connection.commit()
query4 = '''Create table marks (student_id int not null,
                subject_id int not null,
                marks int not null,
                foreign key (student_id) references students(student_id),
                foreign key (subject_id) references subjects(subject_id),
                Primary key (student_id,subject_id));'''
cursor.execute(query4)
connection.commit()
cursor.close()
connection.close()