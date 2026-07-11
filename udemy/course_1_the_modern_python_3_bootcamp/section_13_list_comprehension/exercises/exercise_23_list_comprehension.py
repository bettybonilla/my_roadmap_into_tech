"""
- Given the string “amazing”, create a variable called answer, which is a list
containing all the letters from “amazing” but not the vowels - Use a list
comprehension!
- The answer should look like this: ['m', 'z', 'n', 'g']
"""

amazing = "amazing"
print(amazing)

answer = [char for char in amazing if char not in "aeiou"]
print(answer)

# Alternative code using a for loop
# answer = []

# for char in amazing:
#     if char not in "aeiou":
#         answer.append(char)
# print(answer)
