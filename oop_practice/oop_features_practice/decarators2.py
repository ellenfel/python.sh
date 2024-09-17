class Backpack():

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items

        else:
            print("Enter a valid list")

my_backpack = Backpack()
print(my_backpack.items)

my_backpack.items = ["Diary", "Pen"]
print(my_backpack.items)