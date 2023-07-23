"""
For all the numbers between 1 and 100 (including 100), create a variable
called answer, which contains a list with all the numbers that are divisible
by 12 (Ex: 12, 24, 36, etc.) - Use a list comprehension!
"""

numbers = list(range(1, 101))
print(numbers)

answer = [num for num in numbers if num % 12 == 0]
print(answer)

# Alternative code using a for loop
# answer = []

# for num in numbers:
#     if num % 12 == 0:
#         answer.append(num)
# print(answer)
