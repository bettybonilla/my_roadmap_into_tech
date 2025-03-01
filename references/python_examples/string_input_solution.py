"""
- Create a my_utilities private GitHub repo
- The my_utilities repo should include convenient functions and code snippets
so that you can pull and import it into future projects for your convenience
instead of copying and pasting your code around and to discourage use now to
cement learnings
- You can implement helper functions in your my_utilities file as methods in a
class with OOP or as functions with functional programming
"""

# -----------------------------------------------------------------------------
# TODO: Revisit and finalize then add to my_utilities repo
# -----------------------------------------------------------------------------


def compare_insensitive(s1: str, s2: str):
    return s1.lower() == s2.lower()


class StrExtenstion(str):
    def compare_insensitive(self, other) -> bool:
        return self.lower() == other.lower()


user_input = "string1"
user_input.compare_insensitive("string2")

"string1".compare_insensitive("string2")

# References
# https://www.tutorialsteacher.com/python/string-casefold#:~:text=It%20is%20similar%20to%20the,converts%20it%20to%20'ss'%20
# https://stackoverflow.com/questions/352537/extending-builtin-classes-in-python
