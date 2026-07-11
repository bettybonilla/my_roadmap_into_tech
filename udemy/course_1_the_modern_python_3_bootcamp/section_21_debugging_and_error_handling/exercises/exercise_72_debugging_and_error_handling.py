"""
Now that you've learned about debugging and error handling, let's get some
practice!
- Write a function called divide, which accepts two parameters - You can
call them num1 and num2
    - The function should return the result of num1 divided by num2
    - If you do not pass the correct type of arguments to the function, it
    should return the string "Please provide two integers or floats"
    - If you pass a 0 as the second argument, Python will raise a
    ZeroDivisionError, so if this function is invoked with a 0 as the value of
    num2, return the string "Please do not divide by zero"
        - Ex:
            divide(4, 2)  # 2
            divide([], "1")  # "Please provide two integers or floats"
            divide(1, 0)  # "Please do not divide by zero"
"""


def divide(num1: int | float, num2: int | float) -> int | float:
    try:
        return num1 / num2
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"


print(divide(4, 2))
print(divide([], "1"))
print(divide(1, 0))
