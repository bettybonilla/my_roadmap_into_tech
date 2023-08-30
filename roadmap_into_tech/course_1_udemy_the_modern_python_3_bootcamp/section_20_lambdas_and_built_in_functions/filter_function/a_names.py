"""
The below uses the filter() function to filter only the names starting with an
A from the names list
"""

names = ["Austin", "Penny", "Anthony", "Angel", "Billy"]

a_names = list(filter(lambda name: name[0] == "A", names))
print(a_names)
