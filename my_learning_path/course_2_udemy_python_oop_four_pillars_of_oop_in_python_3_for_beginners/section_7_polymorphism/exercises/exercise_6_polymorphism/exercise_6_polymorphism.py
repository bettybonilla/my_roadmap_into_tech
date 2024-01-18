"""
Create a class called Square and perform the following tasks:
- Create two objects for this class, square_one and square_two
- Find the result of side of square_one to the power of side of square_two
    - Ex: If square_one has a length of 2 cm each side and square_two has a
    length of 4 cm each side, square_one ** square_two should return 16, which
    is 2 to the power of 4
- Hint: While performing square_one ** square_two, you need to overload the
__pow__() method
"""

from typing import Self


class Square:
    def __init__(self, side_cm: int):
        self.side_cm = side_cm

    def __pow__(square_one: Self, square_two: Self) -> int:
        return square_one.side_cm**square_two.side_cm


square_one = Square(2)
square_two = Square(4)
print("square_one to the power of square_two =", square_one**square_two)
