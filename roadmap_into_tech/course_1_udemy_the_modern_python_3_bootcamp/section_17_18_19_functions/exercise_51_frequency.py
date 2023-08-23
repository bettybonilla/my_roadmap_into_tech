"""
Write a function called frequency
- This function accepts a list and a search_term (this will always be a
primitive value) and returns the number of times the search_term appears in
the list
"""


# Primitive data types are data types that store data of only one type
# There are 4 primitive data types in Python: int, float, bool, str
def frequency(your_list: list, search_term: int | float | bool | str) -> int:
    return your_list.count(search_term)


print(frequency([1, 2, 3, 4, 4, 4], 4))
print(frequency([1, 2.5, 6, 9, 2.5, 10], 2.5))
print(frequency([True, False, True, True], False))
print(frequency(["cat", "dog", "bird"], "fish"))
