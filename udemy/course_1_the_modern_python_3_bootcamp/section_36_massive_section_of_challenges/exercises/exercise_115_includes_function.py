"""
- Write a function called includes which accepts a collection, a value, and an optional starting index
    - The function should return True if the value exists in the collection when we search starting from the starting
    index
    - Otherwise, it should return False
    - The collection can be a string, a list, or a dictionary
        - If the collection is a string or array, the third parameter is a starting index for where to search from
        - If the collection is a dictionary, the function searches for the value among values in the dictionary - Since
        objects have no sort order, the third parameter is ignored
- Ex:
    includes([1, 2, 3], 1)  # True
    includes([1, 2, 3], 1, 2)  # False
    includes({'a': 1, 'b': 2}, 1)  # True
    includes({'a': 1, 'b': 2}, 'a')  # False
    includes('abcd', 'b')  # True
    includes('abcd', 'e')  # False
"""

from typing import Any, Optional


def includes(
    collection: str | list | dict,
    search_value: Any,
    starting_index: Optional[Any] = None,
) -> bool:
    if not starting_index:
        if type(collection) is str or type(collection) is list:
            return search_value in collection
        if type(collection) is dict:
            return search_value in collection.values()

    if starting_index:
        return search_value in collection[starting_index:]


# Alternative code
# def includes(
#     collection: str | list | dict,
#     search_value: Any,
#     starting_index: Optional[Any] = None,
# ) -> bool:
#     if type(collection) is dict:
#         return search_value in collection.values()
#     if starting_index is None:
#         return search_value in collection
#     return search_value in collection[starting_index:]


if __name__ == "__main__":
    print(includes([1, 2, 3], 1))
    print(includes([1, 2, 3], 1, 2))
    print(includes({"a": 1, "b": 2}, 1))
    print(includes({"a": 1, "b": 2}, "a"))
    print(includes("abcd", "b"))
    print(includes("abcd", "e"))
