"""
The below shows how you can set up default parameters in a function
"""


# The exponent() function below will only run when you also provide a power
# argument
# Otherwise, you will get an error since the function is expecting an argument
# for the power parameter
def exponent(num, power):
    return num**power


print(exponent(2, 3))
print(exponent(3, 2))
# print(exponent(7))


# Here, the updated exponent() function below has now been given a default
# value for the power parameter and therefore you will not get an error since
# when you run the function without an argument for the power parameter, it
# will just default to 2
def exponent(num, power=2):
    return num**power


print(exponent(2, 3))
print(exponent(3, 2))
print(exponent(7))
