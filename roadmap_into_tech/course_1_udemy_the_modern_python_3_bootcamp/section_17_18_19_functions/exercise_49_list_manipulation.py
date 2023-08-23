"""
Write a function called list_manipulation
- This function should take in four parameters (a list, command, location, and
value)
    - If the command is "remove" and the location is "end", the function
    should remove the last value in the list and return the value removed
    - If the command is "remove" and the location is "beginning", the function
    should remove the first value in the list and return the value removed
    - If the command is "add" and the location is "beginning", the function
    should add the value (fourth parameter) to the beginning of the list and
    return the list
    - If the command is "add" and the location is "end", the function should
    add the value (fourth parameter) to the end of the list and return the list
"""

from typing import Optional


def list_manipulation(
    your_list: list, command: str, location: str, value: Optional[int] = None
):
    if command == "remove" and location == "end":
        return your_list.pop()
    elif command == "remove" and location == "beginning":
        return your_list.pop(0)
    elif command == "add" and location == "beginning":
        your_list.insert(0, value)
        return your_list
    elif command == "add" and location == "end":
        your_list.append(value)
        return your_list


print(list_manipulation([1, 2, 3], "remove", "end"))
print(list_manipulation([1, 2, 3], "remove", "beginning"))
print(list_manipulation([1, 2, 3], "add", "beginning", 20))
print(list_manipulation([1, 2, 3], "add", "end", 30))
