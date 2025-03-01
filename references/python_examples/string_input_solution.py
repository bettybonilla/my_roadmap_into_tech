"""
- This could be included in a my_utilities module and you would also have a
private github repo for it
- The my_utilities module should include convenient functions and code
snippets so that you can import it into your own files for your convenience
instead of copying and pasting your code around
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
