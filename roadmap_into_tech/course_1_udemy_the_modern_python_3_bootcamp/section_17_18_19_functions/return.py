"""
The below shows the difference between using the print() function and using
the return keyword in a function
- Functions are very explicit and will follow exactly what you've instructed
- NOTE: The return keyword is not the same as the print() function
"""


# The print_square_of_7() function below is very explicit and prints the result
# since that's exactly what you've instructed the function to do by using the
# print() function inside the function and then running/calling/invoking the
# print_square_of_7() function
def print_square_of_7():
    print(7**2)


print_square_of_7()


# The return_square_of_7() function below is also very explicit and will return
# the value since you used the return keyword specifically however using the
# return keyword means it will hold the value which is different from
# printing the value so if you want to actually have the value printed, you
# must then use the print() function separately and wrap the function inside
# it or you can assign the function to a variable in order to capture/save the
# value to a variable and then use the print() function with the variable
# wrapped inside it
def return_square_of_7():
    return 7**2
    # As mentioned, any code after the return keyword in a function won't run
    # print("I am after the return keyword!")


print(return_square_of_7())
# Alternative code using a variable
# result = return_7_squared()
# print(result)
