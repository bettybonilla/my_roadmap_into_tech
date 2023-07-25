"""
- Using list comprehension, create a variable called answer with the following
value:
    1. [
    2.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    3.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    4.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    5.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    6.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    7.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    8.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    9.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    10.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    11.  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    12. ]
- It's a 10x10 nested list: 10 rows, each row contains the numbers 0-9
- Don't worry about the formatting/spacing, I just added a bunch of returns to
make things clearer - Your answer will be all on one giant line
- Use nested list comprehension and range to accomplish this
"""

answer = [[num for num in range(0, 10)] for i in range(0, 10)]
print(answer)
