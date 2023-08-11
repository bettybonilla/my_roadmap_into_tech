"""
Now that we've learned about tuples and sets, let's get some practice!
"""

# Create a variable called numbers which is a tuple with the the values
# 1, 2, 3, and 4 inside
numbers = (1, 2, 3, 4)
print(numbers)

# Create a variable called value which is a tuple with the the value 1 inside
value = tuple([1])
# Alternative code
# If you have a single value, just add a comma to make it a tuple since tuples
# expect at least 2 values hence the name tu which phonetically sounds like two
# Although it looks like there's only one value, adding a comma actually
# computes to there being a (single value, NoneType) since, as mentioned, a
# tuple expects at least 2 values and this is why you can't make a tuple with
# a single value without a comma
# value = (1,)
print(value)

# Given the following variable:
values = [10, 20, 30]

# Create a variable called static_values which is the result of the values
# variable converted to a tuple
static_values = tuple(values)
print(static_values)

# Given the following variable:
stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]

# Create a variable called unique_stuff which is a set of only the unique
# values in the stuff list
unique_stuff = set(stuff)
print(unique_stuff)
