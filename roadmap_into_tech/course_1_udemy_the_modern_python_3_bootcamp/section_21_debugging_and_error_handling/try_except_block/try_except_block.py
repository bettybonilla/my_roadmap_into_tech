"""
The below shows how you can use a try/except block to do
error catching/handling in your program
"""

# The try block contains code that may cause an exception/error
try:
    # Raises a NameError since foobar is not defined/assigned
    foobar
# When an exception/error occurs, it is caught by the except block which
# contains code to run when the exception/error occurs
# Below, the except block contains the error type it will raise which will be
# a NameError and the err keyword is used to retrieve the error message which
# is then printed with the print() function
except NameError as err:
    print("Error:", err)
