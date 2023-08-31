"""
The below combines using the map() function and the filter() function to
return a new list with the string “Your instructor is” + each value in the
list but only if the value is less than 5 characters
"""

names = ["Colt", "Rusty", "Lassie"]

instructor = list(
    map(
        lambda name: f"Your instructor is {name}",
        filter(lambda name: len(name) < 5, names),
    )
)
print(instructor)

# Remember that the * star operator is used to "unpack" values in lists and
# tuples however it doesn't only have to be used as an argument to the *args
# parameter in functions
# As we can see, the * star operator "unpacked" the instructor list in the
# print() function and the values were printed - In this case, the "Your
# instructor is Colt" string was printed and is no longer in a list
# For this reason, when the * star operator is used in this way it is also
# known as the unpacking operator :-)
print(*instructor)

# Alternative code using list comprehension
# instructor = [f"Your instructor is {name}" for name in names if len(name) < 5]
# print(instructor)
