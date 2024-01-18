"""
Do you remember Gregor Mendel from biology? We're going to simulate basic
Mendelian inheritance in this exercise - You don't need to know what that
means, but basically imagine a family where all the kids look exactly like one
parent because maybe that parent has more "dominant" genetic traits than the
other parent.
- Create three classes: Mother, Father, and Child
    - Let Mother have the "dominant" traits:
        eye_color = "brown"
        hair_color = "dark brown"
        hair_type = "curly"
    - Let Father have the "recessive" traits:
        eye_color = "blue"
        hair_color = "blonde"
        hair_type = "straight"
- Now define Child to have the same attributes (eye_color, hair_color, and
hair_type) but don't set them on the class - Instead, let Child's MRO (Method
Resolution Order) be such that Child inherits from Mother first, then Father
- NOTE: You don't have to instantiate any of the classes to pass the tests -
The tests will create instances for you
"""


# Base parent class
class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"


# Base parent class
class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blonde"
        self.hair_type = "straight"


# Subclass child class
# Multiple inheritance
class Child(Mother, Father):
    pass


print(Child.mro())
