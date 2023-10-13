"""
- In this exercise x and y are two random variables. The code at the top of
the file randomly assigns them (we'll learn how it works later on) but for now
just leave it alone :)
- If both are positive numbers, print "both positive"
- If both are negative numbers, print "both negative"
- Otherwise, tell us which one is positive and which one is negative
- Ex: "x is positive and y is negative"
- NOTE: The print statements are filled in for you, just add logic - For the
tests to pass, don't change the print statements!
"""

# NO TOUCHING -----------------------------------------------------------------
from random import randint

x = randint(-100, 100)
while x == 0:  # Makes sure x isn't zero
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:  # Makes sure y isn't zero
    y = randint(-100, 100)
# NO TOUCHING -----------------------------------------------------------------

# YOUR CODE GOES HERE:
print("x = {}".format(x))
print("y = {}".format(y))

if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
elif x < 0 and y > 0:
    print("y is positive and x is negative")
