"""
Below is an example of an abstract base class (ABC) without the @abstractmethod
decorator
"""

from abc import ABC


# Abstract base parent class
class Shape(ABC):
    # As mentioned, to signify that the whole class is abstract without
    # forcing implementation of its abstract methods you can just use ABC in
    # the signature of the abstract base class without using @abstractmethod
    # decorators above the abstract methods
    def area(self):
        pass


# Subclass child class AKA derived class
class Square(Shape):
    side = 4

    def area(self) -> int:
        return self.side * self.side


# Subclass child class AKA derived class
class Rectangle(Shape):
    length = 10
    width = 5

    def area(self) -> int:
        return self.length * self.width


s = Square()
print(s.area())
r = Rectangle()
print(r.area())
