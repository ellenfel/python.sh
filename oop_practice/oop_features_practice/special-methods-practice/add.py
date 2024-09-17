class Point2D:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"




my_point = Point2D(56, 60)
print(my_point)