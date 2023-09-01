"""
Write a function called extremes which accepts an iterable
- It should return a tuple containing the minimum and maximum elements
    - Ex:
        extremes([1, 2, 3, 4, 5])  # (1, 5)
        extremes((99, 25, 30, -7))  # (-7, 99)
        extremes("alcatraz")  # ('a', 'z')
"""


def extremes(iterable: str | list | tuple | dict | set) -> tuple:
    return (min(iterable), max(iterable))
    # return type((min(iterable), max(iterable)))


print(extremes([1, 2, 3, 4, 5]))
print(extremes((99, 25, 30, -7)))
print(extremes("alcatraz"))
