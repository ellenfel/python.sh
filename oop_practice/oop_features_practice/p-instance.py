class BackPack:

    def __init__(self, color, size=20):
        self.color = color
        self.size = size
        self.items = []

# instances
my_backpack = BackPack("Blue", 25)
a_backpack = BackPack("Green", 15)
sus_backpack = BackPack("Black", 50)

my_backpack.items = ["Laptop", "I, Robot"]
print(my_backpack.items)
print(my_backpack.color)

a_backpack.items = ["Pen", "notebook"]
print(a_backpack.items)
print(a_backpack.color)

sus_backpack.items = ["Bomb", "How to 9/11"]
print(sus_backpack.items)
print(sus_backpack.color)


###############################
###############################


class Bacteria:

    def __init__(self, x, y, size, shape, have_capsule=False):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape
        self.have_capsule = have_capsule

Amip = Bacteria(15, 1, 3*10e-12, "Bacili")
Thiomargarita_namibiensis = Bacteria(1,4, 75*10e-3, "Cocci")
procaryotes = Bacteria(17, 63, 98*10e-14, "Cocci", True)





