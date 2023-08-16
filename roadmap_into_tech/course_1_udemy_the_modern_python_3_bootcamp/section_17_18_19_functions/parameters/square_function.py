"""
Below we took the return_square_of_7() function and altered it by defining a
new function called square() to accept input so that we can square any number
provided, not just 7
"""


def return_square_of_7():
    return 7**2
    # As mentioned, any code after the return keyword in a function won't run
    # print("I am after the return keyword!")


print(return_square_of_7())


# Parameters are written inside the parentheses of your function’s signature
# line and can be named anything you want just like naming a variable (this is
# why they’re also known as parameter variables) - Make sure you follow the
# same rules of variable naming (lowercase_snake_case, don’t start with a
# number, etc.)
# In the function below, the num parameter represents the number that will be
# provided (the input)
# Then, like the name of the function suggests, when you call the function the
# num parameter (the input) will be multiplied by itself to return the square
# of the number provided
def square(num):
    return num * num
    # Alternative code using exponents **
    # return num**2


print(square(7))
print(square(4))
print(square(8))
