"""
The below shows the difference between the access specifiers/modifiers
"""


# Base parent class
class Car:
    # Public class attribute
    number_of_wheels = 4
    # Protected class attribute
    _color = "Black"
    # Private class attribute
    __year_of_manufacture = 2017


# Subclass child class AKA derived class
class BMW(Car):
    def __init__(self):
        print(f"Public class attribute number_of_wheels: {self.number_of_wheels}")
        print(f"Protected class attribute _color: {self._color}")
        # Raised an error since when you use double underscores for a member
        # (attribute/method) in a class, Python will do name mangling in the
        # background which stores this member as _Car__year_of_manufacture
        # since it is particular to the Car class
        # print(
        #     f"Private class attribute __year_of_manufacture: {self.__year_of_manufacture}"
        # )
        # Since nothing is actually private in Python, you can use the
        # dir() function to return a list of the members of a class to confirm
        # the member name of a class even if it's supposed to be private and
        # then access it with a print statement
        # As mentioned, Python puts members of a class with double underscores
        # in the beginning in alphabetical order
        print(dir(Car))
        print(
            f"Private class attribute __year_of_manufacture: {self._Car__year_of_manufacture}"
        )


bmw = BMW()
