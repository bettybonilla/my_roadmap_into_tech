"""
The below shows how you can create nested lists by using list comprehension
with conditional logic
"""

# Using for i in range(1, 4) prints 3 copies of
# "x" if num % 2 != 0 else "o" for num in range(1, 4) which is ["x", "o", "x"]
# since it will print "x" for odd values and "o" for even values when it loops
# through the range(1, 4)
# Therefore, it prints 3 of the same nested list ["x", "o", "x"] inside the
# tic_tac_toe list
tic_tac_toe = [
    ["x" if num % 2 != 0 else "o" for num in range(1, 4)] for i in range(1, 4)
]
print(tic_tac_toe)
