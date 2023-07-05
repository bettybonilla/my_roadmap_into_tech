"""
Below are different examples of accessing list data with for loops
"""

numbers = list(range(1, 4))
print(numbers)

print("")

numbers = [1, 2, 3, 4]
for number in numbers:
    number = number * 2
    print(number)
print("by value (copy)", numbers)

print("")

numbers = [1, 2, 3, 4]
# Use range(len(list_name)) when you don't know the length of a list
for index in range(len(numbers)):
    print(index)
    # Temporarily updates the values in the list
    copy_of_value_in_index = numbers[index]
    copy_of_value_in_index = copy_of_value_in_index * 100
    print(copy_of_value_in_index)
    # When you use [index] on both sides of the equal = it permanently updates
    # all the values in the list
    numbers[index] = numbers[index] * 2
print("by index (reference)", numbers)

print("")

numbers = [1, 2, 3, 4]
for index, number in enumerate(numbers):
    copy_of_number = numbers[index] * 2
print("by value (copy)", numbers)
