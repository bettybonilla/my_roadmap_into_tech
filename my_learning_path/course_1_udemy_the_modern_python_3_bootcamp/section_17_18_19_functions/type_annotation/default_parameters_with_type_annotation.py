"""
Below the exponent() function includes type annotation/type hinting to clearly
specify the input data type expected for the parameters and the return data
type that can be expected
- NOTE: When giving a default to a parameter, the default should match the
data type already hinted for that parameter
    - Ex: In the exponent() function below, the power parameter was given a
    default of 2, an int, which matches the data type already hinted for the
    power parameter, an int
"""


# Type Annotation/Type Hinting
# In the exponent() function below, it takes 2 integers and returns an integer
# and is annotated as follows:
# The num parameter is expected to be of type int
# The power parameter is expected to be of type int with a default of 2
# The return type is expected to be of type int
def exponent(num: int, power: int = 2) -> int:
    return num**power


print(exponent(2, 3))
print(exponent(3, 2))
print(exponent(7))
