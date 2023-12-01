"""
Write an object-oriented program to create a PreciousStone
- Not more than 5 PreciousStone can be held in possession at a given point of
time
- If there are more than 5 PreciousStone, delete the first stone and store the
new one
"""


class PreciousStone:
    stones = []

    def __init__(self, birthstone: str):
        self.birthstone = birthstone
        PreciousStone.stones.append(birthstone)
        self._only_five_stones()

    @staticmethod
    def _only_five_stones():
        if len(PreciousStone.stones) > 5:
            PreciousStone.stones.pop(0)

    @staticmethod
    def count_stones() -> int:
        return len(PreciousStone.stones)

    @staticmethod
    def get_stones() -> list[str]:
        return PreciousStone.stones


stone1 = PreciousStone("garnet")
stone2 = PreciousStone("amethyst")
stone3 = PreciousStone("aquamarine")
stone4 = PreciousStone("diamond")
stone5 = PreciousStone("emerald")
print(stone1.count_stones())
print(stone1.get_stones())
stone6 = PreciousStone("alexandrite")
print(stone1.count_stones())
print(stone1.get_stones())
stone7 = PreciousStone("ruby")
print(stone1.count_stones())
print(stone1.get_stones())
