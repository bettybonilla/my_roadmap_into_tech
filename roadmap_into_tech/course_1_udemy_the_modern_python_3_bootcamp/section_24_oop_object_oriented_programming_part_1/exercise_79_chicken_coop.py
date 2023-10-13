"""
Suppose we have a big chicken coop in our backyard full of very productive
hens. We're going to model our chickens with python! We want to keep track of
how many eggs each individual chicken lays, and at the same time, we want to
track the total number of eggs all hens have laid.
- Create a Chicken class
    - Each Chicken has a species and a name, as well as an integer attribute
    called eggs that should always start out at 0
    - Each Chicken should also have an instance method called lay_egg which
    should increment and then return that particular Chicken's eggs attribute
        - lay_egg should also increment a class variable called total_eggs
    - The following code should work:
        c1 = Chicken(name = "Alice", species = "Partridge Silkie")
        c2 = Chicken(name = "Amelia", species = "Speckled Sussex")
        Chicken.total_eggs  # 0
        c1.lay_egg()  # 1
        Chicken.total_eggs  # 1
        c2.lay_egg()  # 1
        c2.lay_egg()  # 2
        Chicken.total_eggs  # 3
"""


class Chicken:
    total_eggs = 0

    def __init__(self, name: str, species: str, eggs: int = 0):
        self.name = name
        self.species = species
        self.eggs = eggs

    def lay_egg(self) -> int:
        Chicken.total_eggs += 1
        self.eggs += 1
        return self.eggs


c1 = Chicken(name="Alice", species="Partridge Silkie")
c2 = Chicken(name="Amelia", species="Speckled Sussex")
print(Chicken.total_eggs)
print(c1.lay_egg())
print(Chicken.total_eggs)
print(c2.lay_egg())
print(c2.lay_egg())
print(Chicken.total_eggs)
