import random
import time
from dataclasses import dataclass

from .scraper import QuoteInformation


@dataclass
class GameQuoteDataInformation:
    def __init__(
        self, quote_text: str, author: str, hint_1: str, hint_2: str, hint_3: str
    ):
        self.quote_text = quote_text
        self.author = author
        self.hint_1 = hint_1
        self.hint_2 = hint_2
        self.hint_3 = hint_3


class GameManager:
    def __init__(self, quotes_data: list[QuoteInformation]):
        self.GUESS_LIMIT = 4
        self.quotes_data = quotes_data
        self.used_quote_data_counter = 0
        self.guess_counter = 0
        self.score = 0
        self.shuffle_quotes_data()

    def shuffle_quotes_data(self):
        random.shuffle(self.quotes_data)

    def get_quotes_data(self) -> GameQuoteDataInformation:
        quote_data = self.quotes_data.pop(0)
        self.quotes_data.append(quote_data)
        self.used_quote_data_counter += 1

        quote_text = self.quotes_data[-1].quote_text
        author = self.quotes_data[-1].author
        hint_1 = self.quotes_data[-1].hint_bio
        hint_2 = author.split()[0][0]
        hint_3 = author.split()[-1][0]
        return GameQuoteDataInformation(quote_text, author, hint_1, hint_2, hint_3)

    def check_user_answer_correct(
        self, user_input: str, game_quote_data: GameQuoteDataInformation
    ) -> bool:
        hint = [game_quote_data.hint_1, game_quote_data.hint_2, game_quote_data.hint_3]
        if user_input == game_quote_data.author.lower().strip():
            self.score += 1
            self.guess_counter = 0
            time.sleep(0.5)
            print("\nCorrect, you guessed it! :-)")
            time.sleep(0.5)
            self.display_score_keeping()
            if self.used_all_quote_data():
                time.sleep(0.5)
                print("Congrats, that's all the quotes! :-)\n")
                return True
            return True
        else:
            self.guess_counter += 1
            if user_input == "2" or user_input == "exit" or user_input == "quit":
                if self.score > 0:
                    time.sleep(0.5)
                    self.display_score_keeping()
                    time.sleep(0.5)
                    self.display_exit_message()
                    quit(0)
                else:
                    time.sleep(0.5)
                    print("")
                    self.display_exit_message()
                    quit(0)
            if self.get_guesses_remaining() == 3:
                time.sleep(0.5)
                print("\nIncorrect, try again!\n")
                time.sleep(0.5)
                print("Hint: This person was born on", hint[0])
            if self.get_guesses_remaining() == 2:
                time.sleep(0.5)
                print("\nIncorrect, try again!\n")
                time.sleep(0.5)
                print("Hint:", hint[1], "(First name initial)")
            if self.get_guesses_remaining() == 1:
                time.sleep(0.5)
                print("\nIncorrect, try again!\n")
                time.sleep(0.5)
                print("Hint:", hint[2], "(Last name initial)")
            if self.get_guesses_remaining() <= 0:
                time.sleep(0.5)
                print("\nSorry, you have no more guesses :-(\n")
                time.sleep(0.5)
                print(f"The quote was said by {game_quote_data.author}")
                if self.score > 0:
                    time.sleep(0.5)
                    self.display_score_keeping()
                    time.sleep(0.5)
                    self.display_exit_message()
                    quit(0)
                else:
                    time.sleep(0.5)
                    print("")
                    self.display_exit_message()
                    quit(0)
            return False

    def display_guesses_remaining(self):
        print(f"\nGuesses remaining: {self.get_guesses_remaining()}")

    def get_guesses_remaining(self) -> int:
        return self.GUESS_LIMIT - self.guess_counter

    def display_score_keeping(self):
        print(
            f"\nYou've correctly guessed {self.score} out of {self.get_quotes_data_count()} quotes!\n"
        )

    def get_quotes_data_count(self) -> int:
        return len(self.quotes_data)

    def used_all_quote_data(self) -> bool:
        if self.used_quote_data_counter == self.get_quotes_data_count():
            return True
        return False

    def reset_game(self):
        self.used_quote_data_counter = 0
        self.guess_counter = 0
        self.score = 0

    @staticmethod
    def display_welcome_message():
        print("\nWelcome!\n")
        time.sleep(0.5)
        print("Guess ...")
        time.sleep(0.5)
        print("who ...")
        time.sleep(0.5)
        print("said it!")

    @staticmethod
    def display_game_options():
        print("")
        print("--------------------------------------------------------------------")
        print("Enter 1 to display your current score")
        print("Enter 2 to exit/quit the game")
        print("--------------------------------------------------------------------")
        print("")

    @staticmethod
    def display_next_quote_message():
        positive_words = ["Great", "Awesome", "Amazing", "Fantastic", "Yay"]
        random.shuffle(positive_words)
        positive_word = positive_words.pop(0)

        print(f"\n{positive_word}, here's the next quote!")
        time.sleep(0.5)
        print("")
        print("--------------------------------------------------------------------")
        print("")

    @staticmethod
    def display_exit_message():
        print("Thanks for playing, bye!")
