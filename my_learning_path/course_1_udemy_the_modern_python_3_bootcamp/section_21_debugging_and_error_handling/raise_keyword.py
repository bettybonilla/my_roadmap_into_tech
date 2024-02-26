"""
The below shows how you would use the raise keyword to raise your own
exceptions/errors to help other people using your function call your function
appropriately depending on the particular exception/error you expect might
occur
- NOTE: When you raise an exception, the error message you provide does not
return a str type or a None type, it does not return anything so you would use
the NoReturn type hint in your function’s signature
"""

from typing import NoReturn


# In the colorize() function below, it takes 2 strings and returns a string or
# an error message if an exception is raised which is signified with NoReturn
# This is just an example, it doesn't actually colorize the text
def colorize(text: str, color: str) -> str | NoReturn:
    colors = ("red", "blue", "green", "yellow")

    # When raising your own errors and writing error messages, it's best to do
    # them individually to be more explicit and concise so that it is clear on
    # exactly where the error occurred instead of combining errors
    # For example, don't do: if type(text) != str or type(color) != str:
    # Instead, below they have been raised individually with their own
    # explicit and concise error message
    if type(text) != str:
        raise TypeError("Text must be instance of str")
    if type(color) != str:
        raise TypeError("Color must be instance of str")
    if color not in colors:
        raise ValueError("Color is invalid color")
    return f"Printed {text} in {color}"


print(colorize("hello", "red"))

# For this type of exception/error, we can raise a TypeError
# print(colorize(4, "red"))
# print(colorize("hello", 4))

# For this type of exception/error, we can raise a ValueError
# print(colorize("hello", "purple"))
# print(colorize("hello", "chicken"))

# References
# https://youtu.be/GHa4x7BO25I
