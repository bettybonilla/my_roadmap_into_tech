"""
The below shows 2 ways you can prompt for user input with the print() function
or input() function
"""

# This is one way you can prompt a user to input data by using a seperate line
# with the print() function
print("What's your favorite color?")
data = input()
print("You said " + data)

# This is another way you can prompt a user to input data by using one line
# with the input() function as opposed to using a seperate line with
# the print() function
data = input("What's your favorite color? ")
print("You said " + data)
