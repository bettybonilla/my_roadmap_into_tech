"""
Write a function called multiple_letter_count
- This function takes in one parameter (a string) and returns a dictionary
with the keys being the letters and the values being the count of the letter
    - Here's how it should work:
    multiple_letter_count("awesome")  # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's':
    1, 'w': 1}
- Hint: Use a dictionary comprehension and the .count() method
"""


def multiple_letter_count(word: str) -> dict:
    return {letter: word.count(letter) for letter in word}


print(multiple_letter_count("awesome"))
