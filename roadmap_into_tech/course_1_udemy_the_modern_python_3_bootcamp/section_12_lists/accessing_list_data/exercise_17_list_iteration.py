"""
- I've given you a list called sounds which looks like this:
    - sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
- Write code that loops over the list and adds all the strings together to
form one large combined string (don't add any spaces between them)
- The combined string should be in all UPPERCASE as well
- Save the result in a variable called result
"""

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ""

for sound in sounds:
    result += sound
result = result.upper()
print(result)
# You can also put the result variable with the .upper() method in a
# print() function
# print(result.upper())

# Alternative code using .join() method to join the strings in the sounds list
# together to form one combined string
# print("".join(sounds).upper())
