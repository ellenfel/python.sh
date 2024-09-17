class Circle:

    def __init__(self, radius):
        self.radius = radius

my_circle = Circle(4)
your_circle = my_circle

print(my_circle is your_circle)

print(my_circle.radius)
print(your_circle.radius)

your_circle.radius = 15

print(my_circle.radius)
print(your_circle.radius)