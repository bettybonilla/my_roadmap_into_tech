"""
Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the
string are unique and False otherwise
- Ex:
    - has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False
"""


def has_unique_chars(string: str) -> bool:
    len_string = len(string)
    len_set = len(set(string))
    if len_string == len_set:
        return True
    return False
    # return len_string == len_set


if __name__ == "__main__":
    print(has_unique_chars('abcdefg'))
    print(has_unique_chars('hello'))
    print(has_unique_chars(''))
    print(has_unique_chars('0123456789'))
    print(has_unique_chars('abacadaeaf'))

    """
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False
    """
