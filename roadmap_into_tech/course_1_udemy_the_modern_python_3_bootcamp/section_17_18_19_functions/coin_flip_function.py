"""
Define a function that randomly "flips" a coin to return heads or tails
- Below there are 2 solutions:
    - The first one uses the random.choice() method
    - The second one uses the random.random() method
- NOTE: Remember that all methods are functions so it's fine to call them
functions below :-)
"""

import random


# Uses the choice() function from the random module
def coin_flip():
    coin_flip = random.choice(["heads", "tails"])
    return coin_flip


# If we comment out this print() function then the above function won't run
# since it will be overwritten since the function after it shares the same
# name - It's just like how you would overwrite a variable
print(coin_flip())


# Alternative code using the random() function from the random module
def coin_flip():
    # The random() function generates a random number from 0 to 1
    r = random.random()

    if r < 0.5:
        return "HEADS"
    elif r > 0.5:
        return "TAILS"


print(coin_flip())
