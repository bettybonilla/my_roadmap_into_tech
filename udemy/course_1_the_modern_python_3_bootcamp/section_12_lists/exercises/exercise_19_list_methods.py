"""
Now that we've learned about list methods, let's get some practice! See the
problem statements in the comments below
"""

# Initialize an empty list called instructors
instructors = []

# Add the following strings to the instructors list
# "Colt"
# "Blue"
# "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])
print(instructors)

# Remove the last value in the list
instructors.pop()
print(instructors)
# Alternative code using .remove() method
# instructors.remove("Lisa")
# print(instructors)
# Alternative code using del keyword
# del instructors[2]
# print(instructors)

# Remove the first value in the list
instructors.pop(0)
print(instructors)
# Alternative code using .remove() method
# instructors.remove("Colt")
# print(instructors)
# Alternative code using del keyword
# del instructors[0]
# print(instructors)

# Add the string "Done" to the beginning of the list
instructors.insert(0, "Done")
print(instructors)
