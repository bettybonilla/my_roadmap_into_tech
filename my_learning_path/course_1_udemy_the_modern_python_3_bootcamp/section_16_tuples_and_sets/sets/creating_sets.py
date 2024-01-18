"""
To create a set you can use curly brackets {} similar to dictionaries however
you're not storing key-value pairs so you don't need colons or you can also
create a set with the set() function
- NOTE: As we can see, sets don't allow duplicates so the duplicates in set3
are removed when we print it
"""

set1 = {1, 2, 3}
print(set1)

set2 = set({4, 5, 6})
print(set2)

# Sets don't allow duplicates
set3 = {1, 2, 3, 3, 4, 5, 5, 5}
print(set3)
