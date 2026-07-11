"""
A common use case of using a set is to convert a list that contains duplicates
to a set to remove the duplicates
"""

# List of cities (contains duplicates)
cities = [
    "Los Angeles",
    "Boulder",
    "Kyoto",
    "Paris",
    "Florence",
    "Santiago",
    "Los Angeles",
    "Shanghai",
    "Boulder",
    "San Francisco",
    "Oslo",
    "Tokyo",
]

print(cities)

# Converts/casts the cities list to a set and therefore only prints unique
# cities
unique_cities = set(cities)
print(unique_cities)

# Prints how many unique cities there are
print(len(unique_cities))
# Alternative code using double casting
# print(len(set(cities)))
