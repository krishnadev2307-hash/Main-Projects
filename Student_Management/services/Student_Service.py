"""Here we do the validation part.
The raw input received from the main gets validated,
and accordingly it goes to the repository."""
from Student_Management.models.student import Student

class StudentService:

    def __init__(self,StudentRepository):
        self._StudentRepository = StudentRepository

    @staticmethod
    def present(data:dict)->dict:
        _present = {"student_age": "absent", "branch_id": "absent", "semester": "absent", "attendance": "absent"}
        for key in data:
            if key in _present:
                _present[key] = "present"
        return _present

    @staticmethod
    def _validate_range(data:dict,present:dict)->str:
        error_message = ""
        max_valid_data = {"student_age":22,"branch_id":8,"semester":8,
                          "attendance":100}
        min_valid_data = {"student_age":18,"branch_id":1,"semester":1,
                          "attendance":0}

        for key in present.keys():
            if present[key] == "present":
                if not max_valid_data[key]>=data[key]>=min_valid_data[key]:
                    error_message+=f'{key} is invalid\n'

        return error_message

    @staticmethod
    def _validate_marks(data:dict)->str:
        error_message = ""
        for key in data:
            try:
                if not 0<=data[key]<=100:
                    error_message+=f'{key} has invalid marks\n'
            except KeyError:
                error_message+=f'{key} is not present in DB\n'

        return error_message

    @staticmethod
    def _validate_format(data:dict,fields:dict)->str:
        error_message = ""
        if fields["phone_number"]=="present":
            if len(data["phone_number"])!=10:
                error_message+=f'{data["phone_number"]} is not a valid phone number\n'
            else:
                for digit in data["phone_number"]:
                    if not digit.isdigit():
                        error_message+=f'{data["phone_number"]} is not a valid phone number\n'
                        break
        if fields["email"]=="present":
            Format = {"@gmail.com": 1, "@outlook.com": 1, "@hotmail.com": 1}
            index = data["email"].find("@")
            if index != -1:
                email = data["email"][index:]
                try:
                    Format[email]
                except KeyError:
                    error_message += f'{data["email"]} is not a valid email\n'

            elif index == -1:
                error_message += f'{data["email"]} is not a valid email\n'

        return error_message

    def create_student(self,data:dict)->str:
        present = self.present(data)
        msg1 = self._validate_range(data,present)
        msg2 = self._validate_marks(data["marks"])
        msg3 = self._validate_format(data,{"phone_number":"present","email":"present"})
        final_error_message = ""
        final_error_message+=msg1+msg2+msg3
        if final_error_message=="":
            student = Student(student_name=data["student_name"],
                              student_age=data["student_age"],
                              branch_id=data["branch_id"],
                              semester=data["semester"],
                              marks = data["marks"],
                              attendance=data["attendance"],
                              phone_number=data["phone_number"],
                              email = data["email"],
                              )
            self._StudentRepository.create_student(student)
            return "Student created successfully"

        else:
            return final_error_message

    def get_student_by_id(self,id:int)->list:
        student_data = self._StudentRepository.get_by_id(id)
        return student_data

    def get_all_students(self)->list:
        data = self._StudentRepository.get_all()
        return data

    def update(self,id:int,data:dict)->str:
        Exists = self._StudentRepository.student_exists(id)
        present = self.present(data)
        msg1 = self._validate_range(data,present)
        fields_for_format = {"phone_number":"absent","email":"absent"}
        for key in data:
            try:
                fields_for_format[key] = "present"
            except KeyError:
                pass
        msg2 = self._validate_format(data,fields_for_format)
        if Exists and msg1==msg2=="":
            self._StudentRepository.update_student(id,data)
            return "Student updated successfully"
        else:
            return msg1+msg2+"Student does not exist"

    def delete_student(self,id:int)->str:
        Exists = self._StudentRepository.student_exists(id)
        if Exists:
            self._StudentRepository.delete_student(id)
            return "Student deleted successfully"
        else:
            return "Student does not exist"

    def Marks(self,id:int)->list:
        Exists = self._StudentRepository.student_exists(id)
        if Exists:
            data = self._StudentRepository.get_marks(id)
            return data
        else:
            return []

    def UpdateMarks(self,id:int,data:dict)->str:
        Exists = self._StudentRepository.student_exists(id)
        if Exists:
            result = self._StudentRepository.update_marks(id,data)
            return result
        else:
            return "Student does not exist"