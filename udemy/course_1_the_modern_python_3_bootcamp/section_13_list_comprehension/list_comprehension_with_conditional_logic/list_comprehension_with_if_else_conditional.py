"""
The below shows list comprehension with conditional logic and how you would
use if conditionals and else conditionals
"""

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

# Prints the even numbers in the numbers list
evens = [num for num in numbers if num % 2 == 0]
print(evens)

# Alternative code using a for loop
# evens = []

# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
# print(evens)

# Prints the even numbers multiplied by 2 and the odd numbers divided by 2 in
# the numbers list
evens_odds = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]
print(evens_odds)

# Alternative code using a for loop
# evens_odds = []

# for num in numbers:
#     if num % 2 == 0:
#         evens_odds.append(num * 2)
#     else:
#         evens_odds.append(num / 2)
# print(evens_odds)
