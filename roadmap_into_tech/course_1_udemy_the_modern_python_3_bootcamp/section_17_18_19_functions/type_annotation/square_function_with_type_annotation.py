"""
Below the square() function includes type annotation to clearly specify the
input expected in the num argument and the return type you can expect
"""


# Type annotation
# In the square() function below, it takes and returns an integer and is
# annotated as follows:
# The num argument is expected to be of type int
# The return type is also expected to be of type int
def square(num: int) -> int:
    return num * num
    # Alternative code using exponents **
    # return num**2


print(square(7))
print(square(4))
print(square(8))

# References
# https://docs.python.org/3/library/typing.html
