class Student:

    def __init__(self,student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"Student: {self.name}" \
               f" | Student ID: {self.student_id}" \
               f" | Age: {self.age}" \
               f" | GPA: {self.gpa}"

        
student = Student("BK201", "Mon Mori", 281, 3.76)
print(student)