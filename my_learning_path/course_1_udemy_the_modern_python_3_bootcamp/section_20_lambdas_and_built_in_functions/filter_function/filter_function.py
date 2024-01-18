"""
The below shows how we can use the filter() function
"""

nums = [1, 2, 3, 4]

# The expression inside the lambda needs to be a boolean expression that
# returns True or False in order for the filter() function to filter the
# values into the list
# The x % 2 == 0 expression will return True or False since if the value in
# the nums list is equal to 0, it will be True and if it's not equal to 0, it
# will be False
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
