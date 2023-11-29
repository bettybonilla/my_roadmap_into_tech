"""
The below shows operator overloading and how to overload the + addition
operator in your class
"""


class Square:
    def __init__(self, side_inches: int):
        self.side_inches = side_inches

    # Overloading the + addition operator so that it can add the sides of the
    # s1 and s2 Square instances/objects
    def __add__(s1, s2) -> int:
        return (4 * s1.side_inches) + (4 * s2.side_inches)


s1 = Square(5)
s2 = Square(10)
print("Sum of sides of s1 and s2:", s1 + s2)
