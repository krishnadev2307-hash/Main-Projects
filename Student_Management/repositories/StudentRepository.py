"""So this is where we originally create a student object
after validating the details from services and doing
the CRUD operations"""
import mysql.connector

class StudentRepository:
    def __init__(self,connection):
        self._connection = connection


    def student_exists(self,id:int)->bool:
        cursor = self._connection.cursor()
        cursor.execute("select * from students where student_id=%s",(id,))
        rows = cursor.fetchone()
        if rows==None:
            return False
        return True

    def create_student(self,Student)->None:
        cursor = self._connection.cursor()
        name = Student.student_name
        age = Student.student_age
        branch_id = Student.branch_id
        semester = Student.semester
        phone_no = Student.phone_number
        attendance = Student.attendance
        email = Student.email
        query = ("insert into students (student_name,student_age,"
                 "branch_id,semester,attendance,phone_number,email)"
                 "values(%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(query,(name,age,branch_id,semester,attendance,phone_no,email))
        self._connection.commit()
        marks = Student.marks
        Id = cursor.lastrowid
        rows = []
        subject_ids = {"DBMS":1,"OOPS":2,"ADS":3}
        for subject in marks:
            rows.append((Id,subject_ids[subject],marks[subject]))
        query = ("insert into marks values(%s,%s,%s)")
        cursor.executemany(query,rows)
        self._connection.commit()
        cursor.close()

    def get_by_id(self,id:int)->list:
        cursor = self._connection.cursor()
        query = "select * from students where student_id=%s"
        cursor.execute(query,(id,))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def get_all(self)->list:
        cursor = self._connection.cursor()
        query = """select student_id,student_name,student_age,branch_id,semester,
                attendance,phone_number,email
                 from students"""
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def update_student(self,student_id:int,updates:dict)->None:
        cursor = self._connection.cursor()
        query = "update students set"
        params = []
        values = []
        for key,value in updates.items():
            values.append(value)
            params.append(str(key)+" =%s")
        query = query +" "+",".join(params)
        query+=" where student_id = %s;"
        values.append(student_id)
        cursor.execute(query,values)
        self._connection.commit()
        cursor.close()

    def delete_student(self,student_id:int)->None:
        cursor = self._connection.cursor()
        try:
            query = "delete from marks where student_id=%s"
            cursor.execute(query,(student_id,))
            query = "delete from students where student_id=%s"
            cursor.execute(query,(student_id,))
            self._connection.commit()
        except mysql.connector.Error:
            self._connection.rollback()
        finally:
            cursor.close()

    def get_marks(self,student_id:int)->list:
        cursor = self._connection.cursor()
        try:
            query = '''select subjects.subject_name, marks.marks from 
            marks join subjects on subjects.subject_id=marks.subject_id
            where marks.student_id=%s'''
            cursor.execute(query,(student_id,))
            rows = cursor.fetchall()
        finally:
            cursor.close()
        return rows

    def update_marks(self,student_id:int,marks:dict)->str:
        cursor = self._connection.cursor()
        for key,value in marks.items():
            query = "update marks set marks = %s where subject_id = %s and student_id = %s;"
            cursor.execute(query,(value,key,student_id))
            self._connection.commit()
        return "Student marks updated successfully"