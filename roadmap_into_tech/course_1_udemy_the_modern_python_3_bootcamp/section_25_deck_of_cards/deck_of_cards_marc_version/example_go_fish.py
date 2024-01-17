from abc import abstractmethod
from random import choice, shuffle
from typing import Optional


class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

        try:
            self.id = int(self.value)
        except ValueError:
            if self.value == "Ace":
                self.id = 11
            elif self.value == "King":
                self.id = 12
            elif self.value == "Queen":
                self.id = 13
            elif self.value == "Jack":
                self.id = 14

    def __repr__(self) -> str:
        return f"({self.value} of {self.suit})"

    def __lt__(self, other):
        return self.id < other.id


class Deck:
    def __init__(self):
        self.cards = None
        self.automatic_shuffle = True
        self._create_deck()

    def draw(self) -> Optional[Card]:
        if len(self.cards) > 0:
            return self.cards.pop()
        if self.automatic_shuffle:
            self._create_deck()
            return self.cards.pop()
        return None

    def deck_count(self) -> int:
        return len(self.cards)

    def allow_automatic_shuffle_when_deck_empty(self, automatic_shuffle: bool):
        self.automatic_shuffle = automatic_shuffle

    def _shuffle_deck(self):
        shuffle(self.cards)

    def _create_deck(self):
        numbers = list(range(1, 10))
        numbers.extend(["Ace", "King", "Queen", "Jack"])
        self.cards = [
            Card(str(value), suit)
            for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]
            for value in numbers
        ]
        self._shuffle_deck()


class Player:
    def __init__(self):
        self._current_hand = []

    def is_in_hand(self, guess: Card) -> bool:
        for c in self._current_hand:
            if c.value == guess.value:
                return True
        return False

    def add_hand(self, cards: list[Card]):
        self._current_hand.extend(cards)

    def add_card(self, card: Card):
        self._current_hand.append(card)

    def remove_card(self, card: Card) -> bool:
        card_to_remove = None
        for c in self._current_hand:
            if c.value == card.value:
                card_to_remove = c
                break

        if card_to_remove is None:
            return False

        try:
            self._current_hand.remove(card_to_remove)
            return True
        except ValueError:
            return False

    def hand_is_empty(self) -> bool:
        return len(self._current_hand) == 0

    def guess_card(self) -> bool:
        pass

    def sort_hand(self):
        self._current_hand.sort()

    def get_hand(self) -> list[Card]:
        return self._current_hand

    def get_hand_values(self) -> list[str]:
        return [c.value for c in self._current_hand]

    def __str__(self) -> str:
        return "Player"


class Computer(Player):
    def __str__(self) -> str:
        return "Computer"

    def guess_card(self, player_to_ask: Player) -> bool:
        card_to_guess = choice(self._current_hand)
        msg = str(card_to_guess).split("of")[0].strip()[1:]
        print(f"Do you have any {msg}s")
        count = 0
        while player_to_ask.is_in_hand(card_to_guess):
            player_to_ask.remove_card(card_to_guess)
            self.add_card(card_to_guess)
            count += 1
        return count > 0


class GameState:
    def __init__(self, player_one: Player, player_two: Player, deck: Deck):
        self._player_one = player_one
        self._player_two = player_two
        self._deck = deck
        self._current_turn = choice([self._player_one, self._player_two])
        self._gameover = False
        self._score = {
            self._player_one: 0,
            self._player_two: 0,
        }

    @abstractmethod
    def start_game(self):
        print(f"Starting game: {self._current_turn} goes first")

    @abstractmethod
    def game_loop(self):
        print("game loop")

    def quit_game(self):
        exit(0)


class GoldFish(GameState):
    def start_game(self):
        super().start_game()
        # draw 5 cards for each player
        for i in range(5):
            self._player_one.add_card(self._deck.draw())
            # draw 5 cards for each player
        for i in range(5):
            self._player_two.add_card(self._deck.draw())
        self.game_loop()

    def game_loop(self):
        self._removepairs(self._player_one)
        self._removepairs(self._player_two)
        while not self._gameover:
            if type(self._current_turn) is Player:
                self._current_turn = self._player_two
            else:
                self._computers_turn()
            if (
                self._player_one.hand_is_empty()
                or self._player_two.hand_is_empty()
                or self._deck.deck_count() == 0
            ):
                self._gameover = True
        print(self._score)

    def _computers_turn(self) -> bool:
        # print("DEBUG PLAYER HAND", self._player_one._current_hand)
        # print("DEBUG Computer HAND", self._player_two._current_hand)
        cards_found = self._player_two.guess_card(self._player_one)
        if cards_found == 0:
            print(f"{self._current_turn}: GO FISH")
            self._player_two.add_card(self._deck.draw())
            self._removepairs(self._current_turn)
        else:
            print("HIT")
            self._removepairs(self._current_turn)
        self._current_turn = self._player_one

    def _removepairs(self, player: Player) -> int:
        player.sort_hand()
        print(player.get_hand())
        # REMOVE PAIRS

        # hand= {}
        # for c in player.get_hand():
        # 	try:
        # 		hand[c.value] += 1
        # 	except KeyError:
        # 		hand[c.value] = 1

        # for card, count in hand.items():
        # 	if count % 2 == 0:
        # 		for _ in range(count):
        # 			player.remove_card(card)
        # 			self._score[player] += 1
        # 	else:
        # 		for _ in range(count-1):
        # 			player.remove_card(card)
        # 			self._score[player] += 1

        # if count >= 2:
        # 	for _ in range(count - (count % 2)):
        # 		player.remove_card(card)
        # 	while count > 0:
        # 		count -= 2
        # 		self._score[player] += 1


if __name__ in "__main__":
    game = GoldFish(Player(), Computer(), Deck())
    game.start_game()
