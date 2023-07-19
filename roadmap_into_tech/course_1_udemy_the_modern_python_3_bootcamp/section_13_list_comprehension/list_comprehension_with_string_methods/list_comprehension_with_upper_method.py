"""
The below uses list comprehension and the .upper() method to uppercase each
character as a single string in the string "colt" in the name variable and
generates it in a new list
- NOTE: The .upper() method did not uppercase the whole string because as the
char item variable iterates through the name variable (iterable) it is
representing a single character in the string “colt” and generating each
character as a single string in a new list as it runs through the loop until
it reaches the end of the loop
"""

# Using the list comprehension below, when a string is not in a list the
# .upper() method uppercases each character as a single string and generates
# it in a new list
name_string = "colt"
print(name_string)

uppercase_character = [char.upper() for char in name_string]
print(uppercase_character)

# When a string is in a list, the .upper() method uppercases all the letters
# in a string and generates it in a new list
name_list = ["colt"]
print(name_list)

uppercase_character = [char.upper() for char in name_list]
print(uppercase_character)
