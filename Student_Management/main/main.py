"""The main program handles the user input.
According to the user input, it will show the results."""

from Student_Management.services.Student_Service import StudentService
from Student_Management.repositories.StudentRepository import StudentRepository
from Student_Management.config.database import Database

def main():
    print("Welcome to Student Management System".center(60,'-'))
    Connection = Database()
    connection = Connection.connect()
    repo = StudentRepository(connection)
    service = StudentService(repo)
    while True:
        print("Menu".center(10,'-'))
        print('1.Add student\n2.Get student by student id\n'
              '3.Get all student details\n 4.Update student details\n'
              '5.Remove student details\n6.Get marks of a student\n7.Update marks by id\n8.Exit\n')
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Enter student details: ")
                print("Important: ENTER DETAILS LIKE <VALUE> <VALUE>")
                print("Order is:student name, student age,"
                      "branch_id,semester,attendance,phone_number,email")
                data = {}
                details = input().split()
                data['student_name'] = details[0]
                data['student_age'] = int(details[1])
                data['branch_id'] = int(details[2])
                data['semester'] = int(details[3])
                data['attendance'] = float(details[4])
                data['phone_number'] = details[5]
                data['email'] = details[6]
                print("Enter the marks: ")
                marks = {}
                print('The order is : DBMS,OOPS,ADS')
                details = input().split()
                marks['DBMS'] = int(details[0])
                marks['OOPS'] = int(details[1])
                marks['ADS'] = int(details[2])
                data['marks'] = marks
                if Connection is not None:
                    result = service.create_student(data)
                    print(result)
                else:
                    print("Database connection failed")

            elif choice == 2:
                    print("Enter student id: ")
                    id = int(input())
                    if Connection is not None:
                        result = service.get_student_by_id(id)
                        if len(result) == 0:
                            print("Student not found")
                        else:
                                print('Student details'.center(30,'-'))
                                print('ID | Name | Age | Branch ID| Semester | Attendance | Phone number | Email')
                                print(f'{result[0][0]} | {result[0][1]} | {result[0][2]} | {result[0][3]} | {result[0][4]} | {result[0][5]} | {result[0][6]} | {result[0][7]}')

                    elif Connection is None:
                        print('Database connection failed')
                    Connection.connect()

            elif choice == 3:
                if Connection is not None:
                    result = service.get_all_students()
                    if len(result) == 0:
                        print("Empty Database.")
                    else:
                        print('Student details'.center(30,'-'))
                        print('ID | Name | Age | Branch ID | Semester | Attendance | Phone number | Email')
                        for student in result:
                            print(f'{student[0]} | {student[1]} | {student[2]} | {student[3]} | {student[4]} | {student[5]} | {student[6]} | {student[7]}')
                elif Connection is None:
                    print('Database connection failed')

            elif choice == 4:
                if Connection is not None:
                    id = int(input("Enter the student id you want to update: "))
                    datatypes = {"student_name":str,"student_age":int,"branch_id":int,"semester":int,"attendance":float,"phone_number":str,"email":str}
                    print('Important: ENTER FIELDS LIKE: \nstudent_name\n'
                          'student_age\n'
                          'branch_id\n'
                          'semester\n'
                          'attendance\n'
                          'phone_number\n'
                          'email only, no other input is valid.')
                    print('First enter the fields which you want to update: ')
                    fields = input().split()
                    print('Enter the details according to the fields: ')
                    data = input().split()
                    details = {}
                    for field,detail in zip(fields,data):
                        details[field] = datatypes[field](detail)
                    result = service.update(id,details)
                    print(result)

                elif Connection is None:
                    print('Database connection failed')

            elif choice == 5:
                if Connection is not None:
                    print('Enter the student id which you want to remove: ')
                    id = int(input())
                    result = service.delete_student(id)
                    print(result)

                elif Connection is None:
                    print('Database connection failed')

            elif choice == 6:
                if Connection is not None:
                    print('Enter the student id which you want to get marks: ')
                    id = int(input())
                    marks = service.Marks(id)
                    print("Subject name | Marks")
                    for mark in marks:
                        print(f'{mark[0]} | {mark[1]}')

                elif Connection is None:
                    print('Database connection failed')

            elif choice == 7:
                if Connection is not None:
                    print('Enter the student id which you want to update marks: ')
                    id = int(input())
                    print('Enter the subject ids first: ')
                    ids = input().split()
                    print('Enter the subject marks next: ')
                    marks = input().split()
                    data = {}
                    for Id,mark in zip(ids,marks):
                        data[int(Id)] = int(mark)
                    result = service.UpdateMarks(id,data)
                    print(result)

                elif Connection is None:
                    print('Database connection failed')

            elif choice == 8:
                print('Thankyou for using our management system...')
                Connection.close()
                break

        except ValueError:
            print('Please enter a valid choice from 1 to 8')

if __name__ == '__main__':
    main()