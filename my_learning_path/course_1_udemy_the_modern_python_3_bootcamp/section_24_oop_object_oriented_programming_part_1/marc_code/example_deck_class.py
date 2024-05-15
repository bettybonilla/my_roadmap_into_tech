import random
from abc import abstractmethod


# abstract base parent class
class Deck:
    # private class attribute
    _cards = []

    @abstractmethod
    def shuffle(self):
        # no implementation (does nothing)
        pass

    @abstractmethod
    def draw_card(self):
        # no implementation (does nothing)
        pass

    # concrete method
    def who_am_i(self):
        print("I am a deck")


# subclass child class
class UnoDeck(Deck):
    def __init__(self):
        # instance attribute
        self._cards = ["A", "B", "C", "D"]

    def shuffle(self):
        return random.shuffle(self._cards)

    def draw_card(self):
        return self._cards.pop()

    # overrides the parent method, parent being Deck
    def who_am_i(self):
        print("I am an uno deck")

    # This is a function not a method since below you don't need to create an
    # instance/object
    def game_type() -> str:
        return "uno"


if __name__ in "__main__":
    parent_deck = Deck()
    parent_deck.shuffle()  # does nothing
    card = parent_deck.draw_card()  # does nothing
    print(card)
    parent_deck.who_am_i()  # prints I am a deck

    uno_deck = UnoDeck()
    uno_deck.shuffle()  # shuffles the list of cards
    card = uno_deck.draw_card()  # pops a card from the list
    print(card)
    uno_deck.who_am_i()  # prints I am an uno deck

    # As mentioned this is a function not a method and you don't need to
    # create an instance/object
    UnoDeck.game_type()

# References
# https://www.geeksforgeeks.org/abstract-classes-in-python/
