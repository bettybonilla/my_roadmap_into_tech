"""
- Generate a random number between 1 and 10 using randint(1, 10), storing the
result in the number variable
- Write a while loop to keep regenerating a new random number between 1 and 10
while the random number is not equal to 5
- In order for my tests to work, please add 1 to the i variable each iteration
through the loop
- NOTE: My tests use the i variable to check how many times your loop runs
"""

# Use randint(a, b) to generate a random number between a and b
from random import randint

# Store the random number in here, each time through the loop
number = randint(1, 10)

# The i variable should be incremented by 1 each iteration through the loop
i = 0

while number != 5:
    number = randint(1, 10)
    print(number)
    # Alternative code to show each iteration through the loop
    # print(number, f"loop #: {i + 1}")
    i += 1
