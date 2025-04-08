"""
The below shows the basics of inheritance in Python
"""


# Base parent class
class Animal:
    # Public class attribute
    cool = True

    def make_sound(self, sound: str) -> str:
        return f"This animal says {sound}"


# Subclass child class
class Cat(Animal):
    pass


sadie = Cat()
print(sadie.make_sound("meow"))
print(sadie.cool)
print(Cat.cool)
print(Animal.cool)
print("")

# The isinstance() Python built-in function returns a boolean True or False
# value if an object is an instance of a class or of a subclass
print(isinstance(sadie, Cat))
print(isinstance(sadie, Animal))
print(isinstance(sadie, object))
