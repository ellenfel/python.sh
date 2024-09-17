class Backpack():

    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a valid list")

#my_backpack = Backpack()
#my_backpack.set_items(["pen", "pencil"])
#print(my_backpack.get_items())

class Circle():
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Please enter a valid number")


my_circle = Circle(5.0)
print(my_circle.get_radius())
    