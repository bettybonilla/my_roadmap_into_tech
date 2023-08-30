"""
The below shows how we can use the map() function
"""

nums = [2, 4, 6, 8, 10]

# Below the map() function takes the lambda function and the nums list and
# will call the lambda function on each value in the nums list to double each
# value then return a map object
doubles = map(lambda x: x * 2, nums)

# As we can see when we print the doubles variable, it prints a map object
print(doubles)

# In order to get the values in the doubles variable we an use a for loop to
# print the values
for num in doubles:
    print(num)

# We can also convert the doubles variable into a list to store the values in
# a list
# However, map objects can only be iterated over once so you will see that
# after the for loop above runs then the code below runs, it will just print an
# empty list
doubles = list(doubles)
print(doubles)

# Typically, you would just wrap the map() function inside the data structure
# you intend to convert it into instead of using a for loop
doubles = list(map(lambda x: x * 2, nums))
print(doubles)


# Alternative code using the map() function with a function instead of a
# lambda function
# def double(num: int) -> int:
#     return num * 2


# nums = [2, 4, 6, 8, 10]

# doubles = list(map(double, nums))
# print(doubles)
