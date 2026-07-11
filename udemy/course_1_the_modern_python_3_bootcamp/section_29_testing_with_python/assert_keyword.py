"""
The below shows how we can use the assert keyword along with an optional error message
"""


def add_positive_nums(x: int, y: int) -> int:
    assert x > 0 and y > 0, "Both numbers need to be positive!"
    return x + y


def eat_junk_food(food: str) -> str:
    assert food in [
        "pizza",
        "ice cream",
        "candy",
        "chips",
    ], "Food must be a junk food!"
    return f"NOM NOM NOM I am eating {food}"


if __name__ == "__main__":
    print(add_positive_nums(1, 2))
    # Raises AssertionError: Both numbers need to be positive!
    # print(add_positive_nums(1, -1))
    print("")
    print(eat_junk_food("pizza"))
    # Raises AssertionError: Food must be a junk food!
    # print(eat_junk_food("spinach"))
