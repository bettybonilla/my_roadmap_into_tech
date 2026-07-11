"""
Write a function called titleize which accepts a string of words and returns a new string with the first letter of every
word in the string capitalized
- Ex:
    titleize('this is awesome')  # "This Is Awesome"
    titleize('oNLy cAPITALIZe fIRSt')  # "ONLy CAPITALIZe FIRSt"
"""


def titleize(string: str) -> str:
    string = string.split(" ")
    new_string = ""
    for word in string:
        new_string += word[0].upper() + word[1:] + " "
    return new_string.strip()


# Alternative code using the enumerate() function
# def titleize(string: str) -> str:
#     string = string.split(" ")
#     for i, word in enumerate(string):
#         string[i] = word[0].upper() + word[1:]
#     return " ".join(string)


if __name__ == "__main__":
    print(titleize("this is awesome"))
    print(titleize("oNLy cAPITALIZe fIRSt"))
