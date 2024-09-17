### One-line Docstrings ###

def add (a,b):
    """Return the sum of a and b."""
    return a+b

def print_floyds_triangle(n):
    """Print Floyd'd triangle wit n rows."""
    count = 1

    for i in range (1, n+1):
        for j in range (i):
            print(count, end="")
            count += 1
        print()


### Multi-line Docstrings ###

def make_frequency_dict(sequence):
    """Return a dictionary that maps each element in sequence to its frequency.

    Create a dictionary that maps each element in the list sequence
    to the number of times the element occurs in the list. The element
    will be the key of the key-value pair in the dictionary and its frequency
    will be the value of the key-value pair.

    Argument:
        sequence: A list of values. These values have to be of an
            immutable data type because they will be assigned as the keys
            of the dictionary. For example, they can be integers, booleans,
            tuples, or strings.

    Return:
        A dictionary that maps each element in the list to its frequency.
        For example, this function call:

        make_frequency_dict([1, 6, 2, 6, 2])

        returns this dictionary:

        {1: 1, 6: 2, 2: 2}

    Raise:
        ValueError: if the list is empty.
    """
    if not sequence:
        raise ValueError("The list cannot be empty")

    freq = {}

    for elem in sequence:
        if elem not in freq:
            freq[elem] = 1
        else:
            freq[elem] += 1

    return freq

## Documentation of classes

class Backpack:
	"""A class that represents a Backpack. 

	Attribute:
		items (list): the list of items in the backpack (initially empty).

	Methods:
		add_item(self, item):
			Add the item to the backpack.
		remove_item(self, item):
			Remove the item from the backpack.
		has_item(self, item):
			Return True if the item is in the backpack. Else, return False.
	"""
	def __init__(self):
		self.items = []

	def add_item(self, item):
		self.items.append(item)

	def remove_item(self, item):
		if item in self.items:
			self.items.remove(item)
		else:
			print("This item is not in the backpack")

	def has_item(self, item):
		return item in self.items