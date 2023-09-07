"""
Implement a function is_all_strings that accepts a single iterable and returns
True if it contains ONLY strings - Otherwise, it should return False
- Ex:
    is_all_strings(['a', 'b', 'c'])  # True
    is_all_strings([2, 'a', 'b', 'c'])  # False
    is_all_strings(('hello', 'goodbye'))  # True
"""


def is_all_strings(iterable: str | list | tuple | dict | set) -> bool:
    # Using a generator expression instead of a list comprehension since I
    # don't need to return a list
    return all((type(i) == str for i in iterable))


print(is_all_strings(["a", "b", "c"]))
print(is_all_strings([2, "a", "b", "c"]))
print(is_all_strings(("hello", "goodbye")))
print(is_all_strings("puppies"))
