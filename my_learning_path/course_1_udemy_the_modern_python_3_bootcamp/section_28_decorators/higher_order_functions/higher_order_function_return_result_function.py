"""
The below shows a higher order function which uses another function as its own return result
- NOTE: Inner functions can also access outer function scope
"""

import random


def make_laugh() -> str:
    def get_laugh() -> str:
        laugh_type = random.choice(("hahaha", "lol", "tehehe"))
        return laugh_type

    return get_laugh()


print(make_laugh())
print(make_laugh())
print(make_laugh())
print("")


# As mentioned above, inner functions can also access outer function scope
def make_laugh_at(person: str) -> str:
    def get_laugh() -> str:
        laugh_type = random.choice(("hahaha", "lol", "tehehe"))
        return f"{laugh_type} {person}"

    return get_laugh()


print(make_laugh_at("Linda"))
print(make_laugh_at("Linda"))
print(make_laugh_at("Linda"))
