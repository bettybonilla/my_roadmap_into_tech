"""
Write a function called is_odd_string which returns True if the sum of each character's position in the alphabet in the
string is odd - For example, "a" is in the first position, "b" is in the second position, etc.
- If the sum is even, return False
- Ex:
    is_odd_string('a')  # True
    is_odd_string('aaaa')  # False
    is_odd_string('amazing')  # True
    is_odd_string('veryfun')  # True
    is_odd_string('veryfunny')  # False
"""


def is_odd_string(string: str) -> bool:
    string = string.upper()
    ascii_alphabet_dict = {chr(count): count for count in range(65, 91)}
    string_sum = 0
    for char in string:
        string_sum += ascii_alphabet_dict.get(char)

    if string_sum % 2 == 1:
        return True
    return False


if __name__ == "__main__":
    print(is_odd_string("a"))
    print(is_odd_string("aaaa"))
    print(is_odd_string("amazing"))
    print(is_odd_string("veryfun"))
    print(is_odd_string("veryfunny"))
