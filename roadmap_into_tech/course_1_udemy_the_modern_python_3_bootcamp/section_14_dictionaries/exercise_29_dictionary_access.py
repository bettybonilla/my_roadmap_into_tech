"""
- For this exercise, I've defined some code for you already
    - The food variable will store a randomly chosen food string like
    "gummy bear" or "morning bun" - Some of these items are in the bakery_stock
    dictionary and some are not
    - Your task is to simply print out a string depending on if food is a
    value in bakery_stock
        - If food is contained in bakery_stock print out a string that states
        how many items are left
            - Ex: "3 left" if food is "toffee cookie" or "1 left" if food is
            "morning bun", etc.
        - If food is not contained in bakery_stock, print out "We don't make
        that"
"""

# NO TOUCHING =================================================================
# Picks a random food item
from random import choice

food = choice(
    [
        "cheese pizza",
        "quiche",
        "morning bun",
        "gummy bear",
        "tea cake",
    ]
)

bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25,
}
# NO TOUCHING =================================================================

# YOUR CODE GOES HERE:
if food in bakery_stock:
    print(bakery_stock.get(food), "left")
else:
    print("We don't make that")
