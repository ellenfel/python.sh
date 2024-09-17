from unicodedata import name


class Dog:
    def __init__(self,name,age):
        self._name = name
        self.age = age

    def get_name(self):
        print("Calling the getter")
        return self._name

    def set_name(self,new_name):
        print("Calling the setter ")
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name

        else:
            print("enter a valid name")

    name = property(get_name, set_name)

my_dog = Dog("Nora", 8)
print(f"My dogs name is {my_dog.age} yo")

print("My Dog's name is ",my_dog.get_name())

my_dog.set_name("Norita")
print("My Dog's new name is",my_dog.get_name())