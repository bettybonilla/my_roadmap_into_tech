"""
The below shows how you can use the as keyword to give an alias to functions
in a module
"""

from random import choice as pick_one, randint as magic_num

print(pick_one(["apple", "banana", "kiwi", "durian"]))
print(magic_num(1, 100))
