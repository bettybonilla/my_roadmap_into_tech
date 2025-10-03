"""
Write a program that takes in a topic for dad jokes then outputs one of the following:
- If there is just one dad joke for the topic, that one dad joke is displayed
- If there is more than one dad joke for the topic, a random dad joke is displayed
- If there are no dad jokes for the topic, a message that there are no dad jokes for that topic is displayed
"""

import random

import requests
from pydantic import BaseModel

BASE_URL = "https://icanhazdadjoke.com/search"


class Result(BaseModel):
    id: str
    joke: str


class DadJoke(BaseModel):
    results: list[Result]
    search_term: str
    status: int
    total_jokes: int


def application_logic():
    print("Hey, let me tell you a dad joke! :-)")
    while True:
        user_input_1 = input("Give me a topic: ").lower().strip()
        print("")

        response = requests.get(
            BASE_URL,
            headers={"Accept": "application/json"},
            params={"term": user_input_1},
        )
        dad_joke = DadJoke(**response.json())
        # print(dad_joke.model_dump_json(indent=4))
        # print(dad_joke.results)

        total_dad_jokes = dad_joke.total_jokes
        if total_dad_jokes <= 0:
            print("Sorry, I don't have any dad jokes on this. Please try again!\n")
        if total_dad_jokes == 1 and dad_joke.status == 200:
            print(f"I have 1 dad joke on this! Here you go:")
            print(dad_joke.results.pop(0).joke)
            print("\nSee ya! Hope I made you laugh (or roll your eyes) ;-)")
            quit(0)
        if total_dad_jokes > 1 and dad_joke.status == 200:
            print(f"I have {total_dad_jokes} dad jokes on this! Here's one:")
            random.shuffle(dad_joke.results)
            random_dad_joke = dad_joke.results.pop(0).joke
            print(random_dad_joke)
            while dad_joke.results:
                user_input_2 = (
                    input("\nWant to hear another one on this topic? (y/n): ")
                    .lower()
                    .strip()
                )
                match user_input_2:
                    case "y":
                        positive_words = [
                            "Ok",
                            "Great",
                            "Awesome",
                            "Amazing",
                            "Fantastic",
                            "Yay",
                        ]
                        random.shuffle(positive_words)
                        positive_word = positive_words.pop(0)
                        print(f"\n{positive_word}! Here you go:")
                        another_random_dad_joke = dad_joke.results.pop(0).joke
                        print(another_random_dad_joke)
                    case "n":
                        user_input_3 = (
                            input(
                                "\nWant to hear another one on a different topic? (y/n): "
                            )
                            .lower()
                            .strip()
                        )
                        match user_input_3:
                            case "y":
                                print("")
                                break
                            case "n":
                                print(
                                    "\nSee ya! Hope I made you laugh (or roll your eyes) ;-)"
                                )
                                quit(0)
                            case _:
                                print("Invalid Input")
                    case _:
                        print("Invalid Input")
            else:
                print(
                    "\nI have no more dad jokes on this! Hope I made you laugh (or roll your eyes) ;-)"
                )
                quit(0)


if __name__ == "__main__":
    application_logic()
