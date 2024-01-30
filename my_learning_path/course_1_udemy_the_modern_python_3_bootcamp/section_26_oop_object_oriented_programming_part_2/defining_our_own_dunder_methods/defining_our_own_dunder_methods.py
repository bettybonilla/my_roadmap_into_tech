"""
Below we've defined our own dunder/magic methods to override them to do something
special
"""

from copy import copy
from typing import Self


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

    # The Self type hint allows you to specify that a class instance can be
    # expected
    # The parent2 parameter is expected to be of type Self (Human instance)
    # The return type is also expected to be of type Self (Human instance)
    # The Self type hint also allows you to specify that a class object can be
    # expected by using the type[Self] type hint however there is no use case
    # in this program
    def __add__(self, parent2: Self) -> Self:
        # Checks that the second argument is a Human instance
        if isinstance(parent2, Human):
            return Human(first="Baby", last=self.last, age=0)
        raise TypeError("You can't add that!")

    # As mentioned above, the Self type hint allows you to specify that a
    # class instance can be expected
    # The return type is expected to be of type list[Self] (list of Human
    # instances)
    def __mul__(self, clone_num: int) -> list[Self]:
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
# operator to add 2 Human instances which returns a new Human instance
print(j + k)
print("")

# Above we defined our own __mul__ dunder method to override the *
# multiplication operator to clone a Human instance by the number provided for
# the clone_num argument which returns a list of the clones for that Human
# instance
print(j * 2)
print("")

# Even though we tried to change the first name to Jessica for the Human
# instance in the list at index 1, it changed it for all the Human instances
# since they are all referencing the same object in memory (self) therefore
# the change was applied to all of them
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
