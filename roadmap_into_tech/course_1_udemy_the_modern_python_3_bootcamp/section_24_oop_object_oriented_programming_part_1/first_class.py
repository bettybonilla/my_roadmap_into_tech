"""
Below we've defined our first, very simple class! :-)
- It models a user and shows the basics of class creation and instantiation
"""


# Class creation
class User:
    pass


# Class instantiation
# To instantiate a class you need to create an instance/object of the class and
# to do this you must assign the class to a variable however, similar to how
# you call a function, you need to type the name of the class followed by
# parentheses
# Below, the user1 variable is an instance/object of the User class and is how
# you would instantiate the User class above and since the user1 variable is
# an instance/object, it is also known as an object variable of the User class
# and can be referred to as a User instance or User object
user1 = User()
# Returns the memory address of where the user1 object is located in memory
print(user1)
# Returns <class '__main__.User'> meaning that user1 is of class User
print(type(user1))
# Below, we've instantiated a new User or a new instance of the User class and
# saved it to the user2 object variable and, as mentioned, it is referred to
# as a User instance/object
# The user1 and user2 objects have different memory addresses since they are
# located in different places in memory because, although they are both empty,
# they are not the same since objects are stored in unique addresses/locations
# in memory regardless of their values
user2 = User()
print(user2)
