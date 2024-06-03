"""
Write a function called min_max_key_in_dictionary which returns a list with the lowest key in the dictionary and the
highest key in the dictionary - You can assume that the dictionary will have keys that are numbers
- Ex:
    min_max_key_in_dictionary({2: "a", 7: "b", 1: "c", 10: "d", 4: "e"})  # [1, 10]
    min_max_key_in_dictionary({1: "Elie", 4: "Matt", 2: "Tim"})  # [1, 4]
"""


def min_max_key_in_dictionary(dictionary: dict[int, str]) -> list[int]:
    keys = dictionary.keys()
    return [min(keys), max(keys)]


if __name__ == "__main__":
    print(min_max_key_in_dictionary({2: "a", 7: "b", 1: "c", 10: "d", 4: "e"}))
    print(min_max_key_in_dictionary({1: "Elie", 4: "Matt", 2: "Tim"}))
