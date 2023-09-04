"""
The below shows how you would use the raise keyword to raise your own errors
to help other people using your function call your function appropriately
depending on the particular errors you expect might occur
"""


# In the colorize() function below, it takes 2 strings and returns a string
# This is just an example, it doesn't actually colorize the text
def colorize(text: str, color: str) -> str:
    colors = ("red", "blue", "green", "yellow")

    # When raising your own errors and writing error messages, it's best to do
    # them individually to be more explicit and concise so that it is clear on
    # exactly where the error occurred instead of combining errors
    # For example, don't do: if type(text) != str or type(color) != str:
    # Instead, below they have been raised individually with their own
    # explicit and concise error message
    if type(text) != str:
        raise TypeError("text must be instance of str")
    if type(color) != str:
        raise TypeError("color must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")


colorize("hello", "red")

# For this type of error, we can raise a TypeError
# colorize(4, "red")
# colorize("hello", 4)

# For this type of error, we can raise a ValueError
# colorize("hello", "purple")
# colorize("hello", "chicken")
