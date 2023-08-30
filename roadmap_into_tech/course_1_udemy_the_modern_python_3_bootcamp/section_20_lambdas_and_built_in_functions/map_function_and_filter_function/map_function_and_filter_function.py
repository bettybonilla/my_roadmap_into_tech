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

# Alternative code using list comprehension
# instructor = [f"Your instructor is {name}" for name in names if len(name) < 5]
# print(instructor)
