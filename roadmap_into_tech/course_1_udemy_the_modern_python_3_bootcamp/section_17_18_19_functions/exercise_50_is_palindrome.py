"""
Write a function called is_palindrome
- A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward or forward
- This function should take in one parameter and return True or False
depending on whether it is a palindrome
    - As a bonus, allow your function to ignore whitespace and capitalization
    so that is_palindrome("a man a plan a canal Panama") returns True
"""


def is_palindrome(string: str) -> bool:
    # The .replace() method below removed all whitespaces and replaced it with
    # empty strings (no spaces) in between the characters in the string
    string = string.lower().replace(" ", "")
    # print(string)

    if string == string[::-1]:
        # print(string)
        return True
    return False


print(is_palindrome("testing"))
print(is_palindrome("tacocat"))
print(is_palindrome("hannah"))
print(is_palindrome("robert"))
print(is_palindrome("amanaplanacanalpanama"))
print(is_palindrome("a man a plan a canal Panama"))
