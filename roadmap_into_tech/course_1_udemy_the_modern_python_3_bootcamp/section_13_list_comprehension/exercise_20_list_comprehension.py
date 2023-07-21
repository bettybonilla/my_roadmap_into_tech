"""
- Given a list, ["Elie", "Tim", "Matt"], create a variable called answer,
which is a new list containing the first letter of each name in the list - I
would use list comprehension though you could also loop over manually
- Given a list, [1, 2, 3, 4, 5, 6], create a new variable called answer2,
which is a new list of all the even values - Another good candidate for list
comprehension
"""

names = ["Elie", "Tim", "Matt"]
print(names)

answer = [name[0] for name in names]
print(answer)

# Alternative code using a for loop
# answer = []

# for name in names:
#     answer.append(name[0])
# print(answer)

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

answer2 = [num for num in numbers if num % 2 == 0]
print(answer2)

# Alternative code using a for loop
# answer2 = []

# for num in numbers:
#     if num % 2 == 0:
#         answer2.append(num)
# print(answer2)
