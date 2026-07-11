"""
The below shows how you can create nested lists with list comprehension
"""

# Using for i in range(1, 4) prints 3 copies of num for num in range(1, 4)
# which is [1, 2, 3]
# Therefore, it prints 3 of the same nested list [1, 2, 3] inside the board
# list
board = [[num for num in range(1, 4)] for i in range(1, 4)]
print(board)
