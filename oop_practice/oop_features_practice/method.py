class Backpack:

    def __init__(self):
        self._items = []

    @property 
    #i am yet to understand what 
    # dose @property accomplishes 
    def items(self):
        return self._items

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)

        else:
            print("Enter a valid item")

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)
            return 1
        
        else:
            print("Please provide a valid item")
            return 0

    def has_item(self, item):
        return item in self._items

    def show_item(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))

        else:
            print(self.items)

my_backpack = Backpack()
print(my_backpack.items)

my_backpack.add_multiple_items(["Pen", "notebook", "matara"])
print(my_backpack.items)
