result= 5 + 6
print(result)

result = (5).__add__(6)
print(result)

# Example 1

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


my_point = Point2D(56,60)
print(my_point)


# Example 2

class Student:

    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"Student: {self.name} " \
               f"| Student ID: {self.student_id} " \
               f"| Age: {self.age} " \
               f"| GPA: {self.gpa}"


student = Student("42AB9", "Nora Nav", 34, 3.76)
print(student)