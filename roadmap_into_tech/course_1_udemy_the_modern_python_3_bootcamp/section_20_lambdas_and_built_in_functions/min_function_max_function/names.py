"""
The below uses the min() function and max() function with a generator
expression and lambda functions
"""


names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]

# Returns the min and max of the names list (alphabetically)
print(min(names))
print(max(names))

# Uses a generator expression with the len() function in the min() function
# that returns the length of the shortest name in the names list however it
# does not return the actual name which would be "Tim"
print(min((len(name) for name in names)))

# However we can use a lambda with the len() function in the min() function or
# max() function to return the actual shortest name or the longest name in the
# names list
print(min(names, key=lambda name: len(name)))
print(max(names, key=lambda name: len(name)))
