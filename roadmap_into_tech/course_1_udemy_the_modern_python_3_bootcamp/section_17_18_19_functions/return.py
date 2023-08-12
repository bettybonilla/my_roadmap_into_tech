"""
The below shows the difference between using the print() function and using
the return keyword in a function
- Functions are very explicit and will follow exactly what you've instructed
- NOTE: The return keyword is not the same as the print() function
"""


# The print_7_squared() function below is very explicit and prints the result
# since that's exactly what you've instructed the function to do by using the
# print() function inside the function and then running/calling/invoking the
# function
def print_7_squared():
    print(7**2)


print_7_squared()


# The return_7_squared() function below is also very explicit and will return
# the value since you used the return keyword specifically however using the
# return keyword means it will hold the value which is different from
# printing the value so if you want to actually have the value printed, you
# must then use the print() function separately and wrap the function inside
# it or you can assign the function to a variable in order to capture/save the
# value to a variable and then use the print() function with the variable
# wrapped inside it
# Also, as mentioned any code after the return keyword in function will not run
def return_7_squared():
    return 7**2
    print("I am after the return keyword!")


print(return_7_squared())
# Alternative code using a variable
# result = return_7_squared()
# print(result)
