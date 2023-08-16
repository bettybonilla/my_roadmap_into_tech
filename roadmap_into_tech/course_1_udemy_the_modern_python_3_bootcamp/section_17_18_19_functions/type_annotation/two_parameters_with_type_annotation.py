"""
Below the add() function and the multiply() function both include type
annotation to clearly specify the input expected for their arguments and the
return type you can expect
"""


# Type annotation
# In the add() function below, it takes 2 integers and returns an integer and
# is annotated as follows:
# The a argument is expected to be of type int
# The b argument is expected to be of type int
# The return type is also expected to be of type int
def add(a: int, b: int) -> int:
    return a + b


# To call the function above, provide 2 values separated by a comma
print(add(2, 2))
print(add(2, 4))
print(add(5, 5))


# Type annotation
# In the multiply() function below, it takes 2 integers and returns an integer
# and is annotated as follows:
# The first argument is expected to be of type int
# The second argument is expected to be of type int
# The return type is also expected to be of type int
def multiply(first: int, second: int) -> int:
    return first * second


# To call the function above, provide 2 values separated by a comma
print(multiply(2, 2))
print(multiply(2, 4))
print(multiply(5, 5))

# References
# https://docs.python.org/3/library/typing.html
