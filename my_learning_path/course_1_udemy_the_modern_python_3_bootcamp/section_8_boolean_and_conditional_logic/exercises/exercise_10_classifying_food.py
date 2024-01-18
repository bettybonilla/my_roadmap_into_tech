"""
- I've written some code at the top of the file for you. Please don't touch it,
if you'd like the tests to work :)
- All the code does is randomly set the food variable to either “apple”,
“grape”, “bacon”, “steak”, “worm”, or “dirt”
- When you run the prewritten code, the food variable will be randomly
assigned. Your task is to write code that will classify the food variable.
- If food is set to either “apple” or “grape”, your code should print “fruit”
- If food is set to either “bacon” or “steak”, your code should print “meat”
- If food is set to either “dirt” or “worm”, your code should print “yuck”
"""

# NO TOUCHING -----------------------------------------------------------------
from random import choice

food = choice(["apple", "grape", "bacon", "steak", "worm", "dirt"])
# NO TOUCHING -----------------------------------------------------------------

# YOUR CODE GOES HERE:
print(food)

if food == "apple" or food == "grape":
    print("fruit")
if food == "bacon" or food == "steak":
    print("meat")
if food == "dirt" or food == "worm":
    print("yuck")
