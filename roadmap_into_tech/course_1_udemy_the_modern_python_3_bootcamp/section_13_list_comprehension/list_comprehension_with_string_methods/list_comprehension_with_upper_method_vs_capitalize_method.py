"""
- The below shows how you would use list comprehension and the .upper() method
along with string concatenation to uppercase the first letter in each string
in the friends list
- You can also just use the .capitalize() method to get the same result which
doesn't need string concatenation since the .capitalize() method capitalizes
the first letter in a string whereas the .upper() method is meant to uppercase
all the letters in a string
"""

friends = ["ashley", "matt", "michael"]
print(friends)

# Uses the .upper() method and string concatenation to uppercase the first
# letter in each string in the friends list
# Without the string concatenation, it would return ["A", "M", "M"]
print([friend[0].upper() + friend[1:] for friend in friends])

# Alternative code using the .capitalize() method which is the string method
# you would want to use since the .capitalize() method capitalizes the first
# letter in a string
print([friend.capitalize() for friend in friends])

# As mentioned, the .upper() method uppercases all the letters in a string
print([friend.upper() for friend in friends])
