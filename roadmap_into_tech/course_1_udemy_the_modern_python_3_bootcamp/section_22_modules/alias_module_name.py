"""
The below shows how you can use the as keyword to give an alias to a module
name which you can use to refer to the module instead
"""

import random as rndm

print(rndm.choice(["apple", "banana", "kiwi", "durian"]))
print(rndm.randint(1, 100))
