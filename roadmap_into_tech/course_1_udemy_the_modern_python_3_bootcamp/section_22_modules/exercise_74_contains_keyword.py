"""
Define a function called contains_keyword that accepts any number of string
arguments
- It should return True if any of the arguments are considered Python keywords
    - Ex: "def", "return", "if", etc.
- Otherwise, it should return False
- Python has a built-in module called keyword that contains a function called
iskeyword()
- Import keyword and then use the keyword.iskeyword() function in your own
function to determine if a given string is a keyword
    - Ex:
        contains_keyword("hello", "goodbye")  # False
        contains_keyword("def", "haha", "lol", "chicken", "alaska")  # True
        contains_keyword("four", "for", "if")  # True
        contains_keyword("blah", "doggo", "crab", "anchor")  # False
        contains_keyword("grizzly", "ignore", "return", "False")  # True
- NOTE: Don't just manually check for the keywords you currently know like
return, def, if, and for, etc. The test logic for this exercise will use a
bunch of keywords we haven't covered yet so definitely make sure to import and
use the keyword module to help you! That's the point of this exercise after
all :)
"""

import keyword


def contains_keyword(*args: str) -> bool:
    # Used a generator expression
    return any((i for i in args if keyword.iskeyword(i)))


print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))
print(contains_keyword("four", "for", "if"))
print(contains_keyword("blah", "doggo", "crab", "anchor"))
print(contains_keyword("grizzly", "ignore", "return", "False"))
