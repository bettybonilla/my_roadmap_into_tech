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

    # Commented out to show that it won't raise an error
    # @staticmethod
    # def area() -> int:
    #     return Square.side * Square.side


# Subclass child class AKA derived class
class Rectangle(Shape):
    length = 10
    width = 5

    @staticmethod
    def area() -> int:
        return Rectangle.length * Rectangle.width


s = Square()
print(s.area())
r = Rectangle()
print(r.area())

# However, you don't need to instantiate these classes in order to call these
# methods
# print(Square().area())
# print(Rectangle().area())
