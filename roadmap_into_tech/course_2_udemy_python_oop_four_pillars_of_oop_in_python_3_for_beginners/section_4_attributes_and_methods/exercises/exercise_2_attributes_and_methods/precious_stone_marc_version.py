class PreciousStone:
    stones = [None, None, None, None, None]
    is_full = False

    def __init__(self, birthstone: str):
        # handle the case where the first 5 item have not been taken
        if not PreciousStone.is_full:
            for i in range(len(PreciousStone.stones)):
                if PreciousStone.stones[i] == None:
                    PreciousStone.stones[i] = birthstone
                    return
            PreciousStone.is_full = True
        # move the first item to the back
        PreciousStone.stones = PreciousStone.stones[1:] + PreciousStone.stones[:1]
        # override the last item with the new item
        PreciousStone.stones[len(PreciousStone.stones) - 1] = birthstone

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
