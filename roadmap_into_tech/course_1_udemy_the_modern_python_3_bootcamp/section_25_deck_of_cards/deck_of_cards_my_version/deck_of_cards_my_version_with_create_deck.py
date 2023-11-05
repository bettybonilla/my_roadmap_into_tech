import random
from dataclasses import dataclass


# The @dataclass decorator tells Python that this class is immutable and is
# not supposed to change or be changed - Typically used when a class is just
# being used to hold data/attributes
@dataclass
class Card:
    def __init__(self, value: str | int, suit: str):
        self._value = value
        self._suit = suit

    def __repr__(self) -> str:
        return f"{self._value} of {self._suit}"


class Deck:
    def __init__(self):
        self._create_deck()

    # Returns a string of how many cards remain in the deck
    def __repr__(self) -> str:
        return f"Deck of {len(self._cards)} cards"

    def _create_deck(self):
        self._values = [i for i in range(2, 11)]
        self._values.extend(["Ace", "Jack", "Queen", "King"])
        self._suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        # Creates a Card instance/object for each of the 52 card combinations
        # and saves it to the self._cards private instance list attribute
        self._cards = [
            Card(value, suit) for suit in self._suits for value in self._values
        ]
        # Sanity check to ensure there are 52 cards in the deck
        assert len(self._cards) == 52
        # Shuffles full deck
        self._shuffle_deck()

    # Returns a shuffled full deck
    def _shuffle_deck(self) -> list[Card]:
        if self.deck_count() == 52:
            random.shuffle(self._cards)
            return self._cards
        raise ValueError("Only full decks can be shuffled")

    # Returns a count of how many cards remain in the deck
    def deck_count(self) -> int:
        return len(self._cards)

    # Returns one card from the deck using the _draw private instance method
    def draw_card(self) -> Card:
        return self._draw(1)[0]

    # Returns a list of cards from the deck using the _draw private instance
    # method
    def draw_hand(self, draw_num: int) -> list[Card]:
        return self._draw(draw_num)

    def _draw(self, draw_num: int) -> list[Card]:
        hand = []
        max_draw = min(draw_num, self.deck_count())

        for i in range(max_draw):
            hand.append(self._cards.pop())
            # Creates a shuffled full deck to draw remaining cards if deck
            # runs out of cards
            if self.deck_count() == 0:
                self._create_deck()
                for i in range(draw_num - 52):
                    hand.append(self._cards.pop())
        return hand


deck1 = Deck()
# print(deck1._cards)
# print(deck1.deck_count())
# print(deck1)
# print("")

print(deck1._shuffle_deck())
print(deck1._draw(3))
print(deck1)
print("")

print(deck1.draw_card())
print(deck1)
print(deck1.draw_hand(2))
print(deck1)
print("")

print(deck1.draw_hand(54))
print(deck1)
