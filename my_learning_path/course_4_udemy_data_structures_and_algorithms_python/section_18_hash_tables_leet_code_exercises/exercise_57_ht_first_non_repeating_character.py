"""
You have been given a string of lowercase letters
- Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given
string using a hash table (dictionary) - If there is no non-repeating character in the string, the function should
return None
- Examples
    - If the input string is "leetcode", the function should return "l" because "l" is the first character that appears
    only once in the string
    - Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating
    character in the string
"""

from typing import Optional


def first_non_repeating_char(string: str) -> Optional[str]:
    my_dict = {i: string.count(i) for i in string}
    for key, value in my_dict.items():
        if value == 1:
            return key
    return None


if __name__ == "__main__":
    print(first_non_repeating_char("leetcode"))
    print(first_non_repeating_char("hello"))
    print(first_non_repeating_char("aabbcc"))

    """
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None
    """
