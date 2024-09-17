class MusicSchool:
     
    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": [28, "555-765-452", ["Cello"]],
                "Eric":   [12, "583-356-223", ["Singing"]]}
    
    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.recenue = revenue

    def print_students_data(self):
        for name in MusicSchool.students:
            self.print_student(name)

    def print_student(self, name):
        data = MusicSchool.students[name]
        print("Student: " + name + " who is " + str(data[0]) + " years old and is taking " + str(data[2]))
            
    def add_student(self, name, data):
        MusicSchool.students[name] = data

headquarters = MusicSchool(6, 12000)
headquarters.print_students_data()

headquarters.print_student("Gino")
headquarters.add_student("Jack", [60, "562-234-234", ["Piano", "Flute"]])
headquarters.print_student("Jack")
