"""
Create a dictionary with the key as a vowel in the alphabet and the value as 0
- Your dictionary should look like this:
    {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
- Do this programmatically (using a dictionary comprehension or dictionary
method) rather than hard coding the answer!
"""

# Using .fromkeys() method with a list
answer = {}.fromkeys(["a", "e", "i", "o", "u"], 0)
print(answer)

# Using .fromkeys() method with a string
# answer = {}.fromkeys("aeiou", 0)
# print(answer)

# Using a dictionary comprehension with a list
# answer = {i: 0 for i in ["a", "e", "i", "o", "u"]}
# print(answer)

# Using a dictionary comprehension with a string
# answer = {char: 0 for char in "aeiou"}
# print(answer)
