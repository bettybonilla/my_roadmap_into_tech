"""
- Given two lists, [1, 2, 3, 4] and [3, 4, 5, 6], create a variable called
answer, which is a new list that is the intersection of the two - Your output
should be [3, 4]
    - Hint: Use the in operator to test whether an element is in a list
        - Ex: 5 in [1, 5, 2] is True
        - Ex: 3 in [1, 5, 2] is False
- Given a list of words, ["Elie", "Tim", "Matt"], create a variable called
answer2, which is a new list with each word reversed and in lowercase (use a
slice to do the reversal!) - Your output should be ['eile', 'mit', 'ttam']
"""

numbers1 = [1, 2, 3, 4]
print(numbers1)
numbers2 = [3, 4, 5, 6]
print(numbers2)

answer = [num for num in numbers1 if num in numbers2]
print(answer)

# Alternative code using a for loop
# answer = []

# for num in numbers1:
#     if num in numbers2:
#         answer.append(num)
# print(answer)

names = ["Elie", "Tim", "Matt"]
print(names)

answer2 = [name[::-1].lower() for name in names]
print(answer2)

# Alternative code using a for loop
# answer2 = []

# for name in names:
#     answer2.append(name[::-1].lower())
# print(answer2)
