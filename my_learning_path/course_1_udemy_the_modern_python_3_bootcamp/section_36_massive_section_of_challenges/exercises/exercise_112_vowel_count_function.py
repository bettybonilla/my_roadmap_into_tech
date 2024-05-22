"""
Write a function called vowel_count that accepts a string and returns a dictionary with the keys as the vowels and
values as the count of times that vowel appears in the string
- Ex:
    vowel_count('awesome')  # {'a': 1, 'e': 2, 'o': 1}
    vowel_count('Elie')  # {'e': 2, 'i': 1}
    vowel_count('Colt')  # {'o': 1}
"""


def vowel_count(string: str) -> dict[str, int]:
    return {i: string.lower().count(i) for i in string.lower() if i in "aeiou"}


if __name__ == "__main__":
    print(vowel_count("awesome"))
    print(vowel_count("Elie"))
    print(vowel_count("Colt"))
