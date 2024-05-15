import random


class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = None
        self._create_deck()

    def draw(self) -> Card:
        if len(self.cards) > 0:
            return self.cards.pop()
        self._create_deck()
        return self.cards.pop()

    def deck_count(self) -> int:
        return len(self.cards)

    def _shuffle_deck(self):
        random.shuffle(self.cards)

    def _create_deck(self):
        numbers = list(range(1, 10))
        numbers.extend(["Ace", "King", "Queen", "Jack"])
        self.cards = [
            Card(str(value), suit)
            for suit in ["Heart", "Spade", "Club", "Diamond"]
            for value in numbers
        ]
        self._shuffle_deck()


class GameState:
    pass


if __name__ in "__main__":
    deck = Deck()

    for card in range(53):
        print(deck.draw())
