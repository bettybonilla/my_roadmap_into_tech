"""
Introduction
- Your goal in this exercise is to implement two classes, Card and Deck

Specifications
- Card
    1. Each instance of Card should have a suit
        - "Hearts", "Diamonds", "Clubs", or "Spades"
    2. Each instance of Card should have a value
        - "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
    3. Card's __repr__ method should return the card's value and suit
        - Ex: "A of Clubs", "J of Diamonds", etc.
- Deck
    1. Each instance of Deck should have a cards attribute with all 52
    possible instances of Card
    2. Deck should have an instance method called count which returns a
    count of how many cards remain in the deck
    3. Deck's __repr__ method should return information on how many cards are
    in the deck
        - Ex: "Deck of 52 cards", "Deck of 12 cards", etc.
    4. Deck should have an instance method called _deal which accepts a
    number and removes at most that many cards from the end of the deck - It
    may need to remove fewer if you request more cards than are currently in
    the deck!
        - If there are no cards left, this method should raise a ValueError
        with the message "All cards have been dealt"
    5. Deck should have an instance method called shuffle which will shuffle
    a full deck of cards - If there are cards missing from the deck, this
    method should raise a ValueError with the message "Only full decks can be
    shuffled"
        - shuffle should return the shuffled deck
    6. Deck should have an instance method called deal_card which uses the
    _deal method to deal a single card from the deck and return that single
    card (not in a list)
    7. Deck should have an instance method called deal_hand which accepts a
    number and uses the _deal method to deal a list of cards from the deck and
    return that list of cards
"""

import random


class Card:
    def __init__(self, suit: str, value: str):
        self._suit = suit
        self._value = value

    def __repr__(self) -> str:
        return f"{self._value} of {self._suit}"


class Deck:
    def __init__(self):
        self._suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        self._values = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]
        # Creates a Card instance/object for each of the 52 card combinations
        # and saves it to the self.cards public instance list attribute - Made
        # public to pass instructor's tests
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]
        # Sanity check to ensure there are 52 cards in the deck
        assert len(self.cards) == 52

    # Returns a string of how many cards remain in the deck
    def __repr__(self) -> str:
        return f"Deck of {len(self.cards)} cards"

    # Returns a count of how many cards remain in the deck
    def count(self) -> int:
        return len(self.cards)

    # Returns a shuffled full deck
    def shuffle(self) -> list[Card]:
        if self.count() == 52:
            random.shuffle(self.cards)
            return self.cards
        raise ValueError("Only full decks can be shuffled")

    # Returns one card from the deck using the _deal private instance method
    def deal_card(self) -> Card:
        return self._deal(1)[0]

    # Returns a list of cards from the deck depending on how many cards remain
    # in the deck using the _deal private instance method
    def deal_hand(self, deal_num: int) -> list[Card]:
        return self._deal(deal_num)

    # Private instance method for internal use only since it will be passed in
    # to the deal_card public instance method and the deal_hand public
    # instance method
    def _deal(self, deal_num: int) -> list[Card]:
        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        hand = []
        max_draw = min(deal_num, self.count())
        for i in range(max_draw):
            hand.append(self.cards.pop())
        return hand


deck1 = Deck()
print(deck1.cards)
print(deck1.count())
print(deck1)
print("")

print(deck1.shuffle())
print(deck1._deal(3))
print(deck1)
print("")

print(deck1.deal_card())
print(deck1)
print(deck1.deal_hand(2))
print(deck1)
