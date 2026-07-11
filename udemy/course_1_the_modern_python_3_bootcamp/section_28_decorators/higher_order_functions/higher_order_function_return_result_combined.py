"""
The below shows a higher order function which uses the return result of an inner function to combine it with its own
return result
"""

import random


def greet(person: str) -> str:
    def get_mood() -> str:
        msg = random.choice(("Hello there ", "Go away ", "I love you "))
        return msg

    return get_mood() + person


print(greet("Toby"))
print(greet("Toby"))
print(greet("Toby"))
