import argparse
import os
import time

import jsonpickle

from scripts.game_manager import GameManager
from scripts.scraper import QuoteInformation, retrieve_quotes_and_pickle

SAVED_PICKLE_QUOTES_DATA_LOCATION = "./downloaded_data/data.json"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="quote_guessing_game",
        description="Guess who said the quote",
    )
    parser.add_argument(
        "-d",
        "--download_quotes",
        action="store_true",
        help="Download fresh quotes from the web",
    )
    arguments = parser.parse_args()

    if arguments.download_quotes:
        print("Downloading quotes ...")
        retrieve_quotes_and_pickle()

    def unpickle_quotes_data_file() -> list[QuoteInformation]:
        with open(SAVED_PICKLE_QUOTES_DATA_LOCATION, "r") as file:
            pickle_quotes_data = file.read()
            unpickle_quotes_data = jsonpickle.decode(pickle_quotes_data)
            return unpickle_quotes_data

    pickle_quotes_data_file_exists = os.path.isfile(SAVED_PICKLE_QUOTES_DATA_LOCATION)
    if pickle_quotes_data_file_exists:
        quotes_data = unpickle_quotes_data_file()
    else:
        retrieve_quotes_and_pickle()
        quotes_data = unpickle_quotes_data_file()

    # Application logic
    game_manager = GameManager(quotes_data)
    time.sleep(0.5)
    game_manager.display_welcome_message()
    time.sleep(0.5)
    game_manager.display_game_options()
    time.sleep(0.5)
    print("Quote:\n")
    game_quote = game_manager.get_quote_data()
    print(f'"{game_quote.quote_text}"')
    time.sleep(0.5)
    game_manager.display_guesses_remaining()
    user_input_1 = input("Enter your answer here: ").lower().strip()

    while True:
        match user_input_1:
            case "1":
                time.sleep(0.5)
                game_manager.display_score_keeping()
                user_input_1 = input("Enter your answer here: ").lower().strip()
            case "2" | "exit" | "quit":
                if game_manager.score > 0:
                    time.sleep(0.5)
                    game_manager.display_score_keeping()
                    time.sleep(0.5)
                    game_manager.display_exit_message()
                    quit(0)
                else:
                    time.sleep(0.5)
                    print("")
                    game_manager.display_exit_message()
                    quit(0)

        if game_manager.check_user_answer_correct(user_input_1, game_quote):
            while True:
                if not game_manager.used_all_quote_data():
                    user_input_2 = (
                        input("Do you want to continue playing? (y/n): ")
                        .lower()
                        .strip()
                    )
                    match user_input_2:
                        case "y":
                            time.sleep(0.5)
                            game_manager.display_next_quote_message()
                            time.sleep(0.5)
                            print("Quote:\n")
                            game_quote = game_manager.get_quote_data()
                            print(f'"{game_quote.quote_text}"')
                            time.sleep(0.5)
                            game_manager.display_guesses_remaining()
                            user_input_1 = (
                                input("Enter your answer here: ").lower().strip()
                            )
                            break
                        case "n" | "2" | "exit" | "quit":
                            time.sleep(0.5)
                            game_manager.display_score_keeping()
                            time.sleep(0.5)
                            game_manager.display_exit_message()
                            quit(0)
                        case _:
                            time.sleep(0.5)
                            print(
                                "\nInvalid Input: Enter y to continue playing or n to exit/quit the game\n"
                            )
                            time.sleep(0.5)
                else:
                    user_input_3 = (
                        input("Do you want to restart the game? (y/n): ")
                        .lower()
                        .strip()
                    )
                    match user_input_3:
                        case "y":
                            game_manager.reset_game()
                            time.sleep(0.5)
                            game_manager.display_welcome_message()
                            time.sleep(0.5)
                            game_manager.display_game_options()
                            time.sleep(0.5)
                            print("Quote:\n")
                            game_quote = game_manager.get_quote_data()
                            print(f'"{game_quote.quote_text}"')
                            time.sleep(0.5)
                            game_manager.display_guesses_remaining()
                            user_input_1 = (
                                input("Enter your answer here: ").lower().strip()
                            )
                            break
                        case "n" | "2" | "exit" | "quit":
                            time.sleep(0.5)
                            print("")
                            game_manager.display_exit_message()
                            quit(0)
                        case _:
                            time.sleep(0.5)
                            print(
                                "\nInvalid Input: Enter y to restart or n to exit/quit the game\n"
                            )
                            time.sleep(0.5)
        else:
            time.sleep(0.5)
            game_manager.display_guesses_remaining()
            user_input_1 = input("Enter your answer here: ").lower().strip()
