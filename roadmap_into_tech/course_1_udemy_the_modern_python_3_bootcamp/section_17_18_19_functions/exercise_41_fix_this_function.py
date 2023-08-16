"""
The pre-written count_dollar_signs function is broken
- It's supposed to return the number of $ characters in a given string
    - Ex: count_dollar_signs("$uper $ize") should return 2
    - But for some reason, the function always returns either 0 or 1 - What's
    going on?
- Without adding any new lines, just move existing code around and make it
work as intended
"""


# Broken code
# def count_dollar_signs(word):
#     count = 0
#     for char in word:
#         if char == "$":
#             count += 1
#         return count


# print(count_dollar_signs("$uper $ize"))


# Fixed code
def count_dollar_signs(word):
    count = 0

    for char in word:
        if char == "$":
            count += 1
    return count


print(count_dollar_signs("$uper $ize"))


# Fixed code with type annotation
# def count_dollar_signs(word: str) -> int:
#     count = 0

#     for char in word:
#         if char == "$":
#             count += 1
#     return count


# print(count_dollar_signs("$uper $ize"))
