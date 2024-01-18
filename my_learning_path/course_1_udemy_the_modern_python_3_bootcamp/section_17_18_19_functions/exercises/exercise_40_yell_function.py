"""
Implement a function, yell(), which accepts a single string argument
- It should return (not print) an uppercased version of the string with an
exclamation point added at the end
    - Ex:
        yell("go away")  # "GO AWAY!"
        yell("leave me alone")  # "LEAVE ME ALONE!"
- You do not need to call the function to pass the tests
"""


# Using an f-string
def yell(text: str) -> str:
    return f"{text}!".upper()


print(yell("go away"))


# Alternative code using an f-string
# def yell(text: str) -> str:
#     return f"{text.upper()}!"


# print(yell("go away"))


# Alternative code using the .format() method
# def yell(text: str) -> str:
#     return "{}!".format(text.upper())


# print(yell("go away"))


# Alternative code using string concatenation
# def yell(text: str) -> str:
#     return text.upper() + "!"


# print(yell("go away"))
