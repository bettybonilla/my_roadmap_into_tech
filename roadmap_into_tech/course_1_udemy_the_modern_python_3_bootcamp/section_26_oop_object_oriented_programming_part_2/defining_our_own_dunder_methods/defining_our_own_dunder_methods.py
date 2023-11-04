"""
Below we've defined our own dunder methods to override them to do something
special
"""

from __future__ import annotations
from copy import copy

# from copy import deepcopy


class Human:
    def __init__(self, first: str, last: str, age: int):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self) -> str:
        return f"Human named {self.first} {self.last}, age {self.age}"

    def __len__(self) -> int:
        return self.age

    def __add__(self, parent2: Human) -> Human:
        # Checks that the second argument is a Human instance/object
        if isinstance(parent2, Human):
            return Human(first="Baby", last=self.last, age=0)
        raise TypeError("You can't add that!")

    def __mul__(self, clone_num: int) -> list[Human]:
        if isinstance(clone_num, int):
            # return [self for i in range(clone_num)]
            return [copy(self) for i in range(clone_num)]
            # return [deepcopy(self) for i in range(clone_num)]
        raise TypeError("You can't multiply that!")


j = Human("Jenny", "Larsen", 37)
k = Human("Kevin", "Jones", 39)
print(j)
print(len(j))
print("")


# Above we defined our own __add__ dunder method to override the + addition
# operator to add 2 Human instances/objects which returns a new Human
# instance/object
print(j + k)
print("")

# Above we defined our own __mul__ dunder method to override the *
# multiplication operator to clone a Human instance/object by the number
# provided for the clone_num argument which returns a list of the clones for
# that Human instance/object
print(j * 2)
print("")

# Even though we tried to change the first name to Jessica for the Human
# instance/object in the list with the index of 1, it changed it for all the
# Human instances/objects since they are all referencing the same object in
# memory (self) therefore the change was applied to all of them
# In order to separate the objects in memory so that they're copies instead of
# being the exact same object, we would import the built-in Python copy.copy
# module then pass self into the copy() function and now they will each be
# copies and be separate objects in memory which means they will be stored in
# their own unique addresses/locations in memory
# However, the copy.copy module makes shallow copies - If you have complex
# classes (child classes, recursion, etc.) it will not copy everything
# Instead, the copy.deepcopy module should be used in these cases since it
# will recursively copy everything however it is slower and uses more memory
three_clones = j * 3
three_clones[1].first = "Jessica"
print(three_clones)
