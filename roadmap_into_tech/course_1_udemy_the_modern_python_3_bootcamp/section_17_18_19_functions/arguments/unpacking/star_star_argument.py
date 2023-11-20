"""
The below shows how we can use the ** star star operator as an argument to
pass in and "unpack" key-value pairs in dictionaries as separate individual
keyword arguments to the parameters in a function
"""


def get_names(first: str, second: str) -> str:
    return f"{first} says hello to {second}"


print(get_names(first="Charlie", second="Sue"))

names = {"first": "Colt", "second": "Rusty"}

# The ** star star operator can be used as an argument with dictionaries and
# will pass in and "unpack" each key-value pair as a separate individual
# keyword argument to the parameters in the function
print(get_names(**names))
