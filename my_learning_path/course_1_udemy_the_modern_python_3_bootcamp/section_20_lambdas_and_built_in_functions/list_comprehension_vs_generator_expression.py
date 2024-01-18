"""
The below shows the difference in memory between using a list comprehension vs.
a generator expression
"""

import sys

# The sys.getsizeof() function gets the size in bytes of memory being used
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_expression = sys.getsizeof((x * 10 for x in range(1000)))

# Using generator expressions are more memory efficient than using list
# comprehensions
print("To do the same thing, it took...")
print(f"List comprehension: {list_comp} bytes")
print(f"Generator expression: {gen_expression} bytes")
