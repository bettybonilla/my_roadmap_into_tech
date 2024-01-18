"""
Write a function called single_letter_count
- This function takes in two parameters (two strings)
    - The first parameter should be a word and the second should be a letter
    - The function returns the number of times that letter appears in the word
    - The function should be case insensitive (does not matter if the input is
    lowercase or uppercase)
    - If the letter is not found in the word, the function should return 0
- Hint: Take advantage of the .count() method
"""


def single_letter_count(word: str, letter: str) -> int:
    return word.lower().count(letter.lower())


# Alternative code however you don't need to create a list since a string is a
# "list" of characters therefore all built-in list methods will work on strings
# def single_letter_count(word: str, letter: str) -> int:
#     letter_count = list(word.lower())
#     letter_count = letter_count.count(letter)
#     return letter_count


print(single_letter_count("Hello World", "h"))
print(single_letter_count("Hello World", "z"))
print(single_letter_count("Hello World", "l"))
