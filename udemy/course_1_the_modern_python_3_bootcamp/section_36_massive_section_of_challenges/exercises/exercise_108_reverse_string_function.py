"""
Write a function called reverse_string which accepts a string and returns a new string with all the characters reversed
- Ex:
    reverse_string('awesome')  # 'emosewa'
    reverse_string('Colt')  # 'tloC'
    reverse_string('Elie')  # 'eilE'
"""


def reverse_string(string: str) -> str:
    return string[::-1]


if __name__ == "__main__":
    print(reverse_string("awesome"))
    print(reverse_string("Colt"))
    print(reverse_string("Elie"))
