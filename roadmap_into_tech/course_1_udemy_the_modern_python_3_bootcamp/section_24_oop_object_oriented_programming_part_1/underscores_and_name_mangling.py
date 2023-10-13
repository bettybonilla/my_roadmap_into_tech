"""
The below shows the difference between using a single underscore vs. double
underscores in front of an attribute (also applies to methods) and what name
mangling does and is used for
"""


class Person:
    def __init__(self):
        self.name = "Tony"
        # As mentioned, using a single underscore in front of an attribute
        # (or method) is a naming convention (suggestion) to signify to other
        # developers that it is private (intended for internal use only) and
        # not meant to be used outside of the class however, as you see below,
        # it can still be accessed
        self._secret = "hi!"
        # When you use double underscores in front of an attribute (or method),
        # Python will mangle the name in the background
        # Below the dir() function is used to show what happens
        # However, you can still access attributes (or methods) with double
        # underscores since nothing is actually private in Python and name
        # mangling is only used to make an attribute or method with double
        # underscores particular to a class so that if there's another class
        # with the same attribute or method name, there is no naming conflict
        self.__msg = "I like turtles!"
        self.__lol = "HAHAHA"


p = Person()
print(p.name)

# As mentioned above, the _secret private attribute can still be accessed
print(p._secret)

# Raises an AttributeError: 'Person' object has no attribute '__msg'
# print(p.__msg)

# The dir() function returns a list of the attributes and methods of an object
# Python will put attributes or methods with double underscores in the
# beginning as "_ClassName__attributeORmethod"
# print(dir(p))

# As mentioned above, these private attributes can still be accessed since
# nothing is actually private in Python
print(p._Person__msg)
print(p._Person__lol)
