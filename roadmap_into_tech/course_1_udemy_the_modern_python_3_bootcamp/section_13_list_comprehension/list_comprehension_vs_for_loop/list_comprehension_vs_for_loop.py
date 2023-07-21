"""
The below shows list comprehension vs. for loops to get the same result
"""

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Uses list comprehension to double each number in the numbers list
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

# Alternative code using a for loop
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)
print(doubled_numbers)
