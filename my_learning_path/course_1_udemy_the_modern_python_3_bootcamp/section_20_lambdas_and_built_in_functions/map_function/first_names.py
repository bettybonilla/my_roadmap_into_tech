"""
The below uses the map() function to get the first names from the names list
"""

names = [
    {"first": "Colt", "last": "Steele"},
    {"first": "Rusty", "last": "Steele"},
    {"first": "Blue", "last": "Steele"},
]

first_names = list(map(lambda x: x["first"], names))
print(first_names)
