from unicodedata import name


class Dog:

    species = "canis lupus"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

print(Dog.species)


class BackPack:

    max_num_items = 10

    def __init__(self, color, size=20):
        self.color = color
        self.size = size
        self.items = []

my_backpack = BackPack("Blue", 25)
your_backpack = BackPack("Green", 15)