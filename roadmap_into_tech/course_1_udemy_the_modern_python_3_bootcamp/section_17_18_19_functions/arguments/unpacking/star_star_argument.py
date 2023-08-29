"""
The below shows how we can use the ** star star operator as an argument to
"unpack" key-value pairs in dictionaries into separate individual keyword
arguments
"""


def display_names(first: str, second: str) -> str:
    return f"{first} says hello to {second}"


print(display_names(first="Charlie", second="Sue"))

names = {"first": "Colt", "second": "Rusty"}

# The ** star star operator can be used as an argument with dictionaries and
# will pass in and "unpack" each key-value pair as a separate individual
# keyword argument to the parameters in the function
print(display_names(**names))
