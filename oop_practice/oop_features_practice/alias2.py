class Backpack:

    def __init__(self):
        self._items = []

    @property  
    def items(self):
        return self._items

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)        
        else:
            print("Item is not in backpack")


my_backpack = Backpack()
your_backpack = my_backpack
her_backpack = your_backpack

print(my_backpack is your_backpack is her_backpack)

my_backpack.add_item("Coffee")
my_backpack.add_item("Pen")

print(my_backpack.items)
print(your_backpack.items)
print(her_backpack.items)

o = [5, 2, 7, 9, 0]
p = o
a = p
c = o
b = c

print(o is p is a is c is b)