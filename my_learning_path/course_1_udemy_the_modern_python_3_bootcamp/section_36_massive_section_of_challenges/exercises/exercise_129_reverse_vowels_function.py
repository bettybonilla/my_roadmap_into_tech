"""
- Write a function called reverse_vowels
    - This function should reverse the vowels in a string
    - Any characters which are not vowels should remain in their original position - You should not consider "y" to be
    a vowel
- Ex:
    reverse_vowels("Hello!")  # "Holle!"
    reverse_vowels("Tomatoes")  # "Temotaos"
    reverse_vowels("Reverse Vowels In A String")  # "RivArsI Vewols en e Streng"
    reverse_vowels("aeiou")  # "uoiea"
    reverse_vowels("why try, shy fly?")  # "why try, shy fly?"
"""


def reverse_vowels(string: str) -> str:
    vowels = []
    for char in string:
        if char in "aeiouAEIOU":
            vowels.append(char)
    vowels.reverse()

    reversed_vowels_string = ""
    for char in string:
        if char not in "aeiouAEIOU":
            reversed_vowels_string += char
        else:
            reversed_vowels_string += vowels.pop(0)
    return reversed_vowels_string


if __name__ == "__main__":
    print(reverse_vowels("Hello!"))
    print(reverse_vowels("Tomatoes"))
    print(reverse_vowels("Reverse Vowels In A String"))
    print(reverse_vowels("aeiou"))
    print(reverse_vowels("why try, shy fly?"))
