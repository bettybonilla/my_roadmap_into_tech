"""
Below is an example of an abstract base class (ABC) with the @abstractmethod
decorator
"""

from abc import ABC, abstractmethod


# Abstract base parent class
class Shape(ABC):
    # As mentioned, in order to force implementation of an abstract method
    # inside the abstract base class you use ABC in the signature of the
    # abstract base class and the @abstractmethod decorator right above the
    # abstract method which will raise an error if the abstract method is not
    # implemented in a derived class
    @abstractmethod
    def area(self):
        pass


# Subclass child class AKA derived class
class Square(Shape):
    side = 4

    # Commented out to purposely raise an error
    # def area(self) -> int:
    #     return self.side * self.side


# Subclass child class AKA derived class
class Rectangle(Shape):
    length = 10
    width = 5

    def area(self) -> int:
        return self.length * self.width


s = Square()
# Commented out to purposely raise an error
# print(s.area())
r = Rectangle()
print(r.area())

# However, you don't need to instantiate these classes in order to call these
# methods
# print(Square().area())
# print(Rectangle().area())
