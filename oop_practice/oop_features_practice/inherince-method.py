class Teacher:

    def __init__(self,full_name, teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id

    def welcome_student(self):
        print(f"i am {self.full_name} And i hate my job")


class ScienceTeacher(Teacher):
    
    def welcome_student(self):
        print("Science is amazing")
        print(f"Teaching is okay. And my name is {self.full_name}")

mst = ScienceTeacher("walter white", "8888")
mst.welcome_student()
        