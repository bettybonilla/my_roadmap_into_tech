"""
The below shows the difference between using list comprehension vs. for loops
when iterating over a range in a list to multiply the even numbers by 2
"""

numbers = list(range(1, 11))
print(numbers)

# Uses list comprehension to multiply the even numbers by 2 in the numbers list
print([i * 2 for i in numbers if i % 2 == 0])

# Alternative code using a for loop
numbers2 = []

for i in numbers:
    if i % 2 == 0:
        numbers2.append(i * 2)
print(numbers2)
