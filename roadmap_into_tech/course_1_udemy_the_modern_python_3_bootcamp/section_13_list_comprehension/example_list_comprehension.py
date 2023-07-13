numbers = list(range(1, 11))
print(numbers)

# Uses list comprehension to multiply the even numbers by 2 in the numbers list
print([i * 2 for i in numbers if i % 2 == 0])

# Alternative code using for loop
numbers2 = []

for i in numbers:
    if i % 2 == 0:
        numbers2.append(i * 2)
print(numbers2)
