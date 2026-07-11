"""
Write a function called repeat which accepts a string and a number and returns a new string with the string passed to
the function repeated the number amount of times - Do not use the built-in .repeat() method!
- Ex:
    repeat('*', 3)  # '***'
    repeat('abc', 2)  # 'abcabc'
    repeat('abc', 0)  # ''
"""


def repeat(string: str, repeat_num: int) -> str:
    if repeat_num > 0:
        return string * repeat_num
    return ""


if __name__ == "__main__":
    print(repeat("*", 3))
    print(repeat("abc", 2))
    print(repeat("abc", 0))
