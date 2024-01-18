"""
Below we took the square() function and made it into a lambda function, AKA an
anonymous function
"""


def square(num: int) -> int:
    return num * num
    # Alternative code using exponents **
    # return num**2


print(square(7))
print(square(4))
print(square(8))

print("")

# Lambda function
# lambda num: num * num

# Lambda function assigned to a variable however, typically you don’t assign
# lambdas to variables
square_lambda = lambda num: num * num

print(square_lambda(7))
print(square_lambda(4))
print(square_lambda(8))
