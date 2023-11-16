"""
The below is an example of the 3 things we can use to organize a class:
- Class (Noun)
- Attributes (Adjective)
- Methods (Verb)
"""


class SuperHero:
    def __init__(self, cape_color: str):
        self.cape_color = cape_color

    def fly(self) -> bool:
        return True


superman = SuperHero("red")
print(superman.fly())
