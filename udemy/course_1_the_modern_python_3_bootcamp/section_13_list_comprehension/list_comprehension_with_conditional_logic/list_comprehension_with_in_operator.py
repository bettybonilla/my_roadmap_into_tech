"""
The below shows list comprehension with the in membership operator and an
if conditional to check for vowels in a string and join the string without the
vowels using the .join() method
"""

with_vowels = "This is so much fun!"
print(with_vowels)

# The in membership operator checks for vowels in the string in the
# with_vowels variable with the if conditional which says that if the
# char item variable is not a vowel while looping through the string, join the
# string without the vowels using the .join() method
print("".join(char for char in with_vowels if char not in "aeiou"))

# Alternative code using a for loop
# without_vowels = ""

# for char in with_vowels:
#     if char not in "aeiou":
#         without_vowels += char
# print("".join(without_vowels))
