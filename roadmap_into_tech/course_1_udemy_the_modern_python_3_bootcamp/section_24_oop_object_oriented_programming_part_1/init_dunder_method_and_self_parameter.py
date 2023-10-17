"""
Below we took our first class, the empty User class, and initialized data
(attributes) that each User instance/object should have using the __init__
dunder method and the self parameter
"""


# The below is to show that Python automatically runs the code inside the
# __init__ dunder method when you create a new instance of a class
# class User:
#     def __init__(self):
#         print("A new user has been made!")


# user1 = User()
# user2 = User()

# However the above was just to prove that Python automatically runs the code
# inside the __init__ dunder method since you wouldn't actually use print
# statements in __init__ dunder methods
# Instead, you would use the __init__ dunder method to set and initialize the
# data (attributes) that each User instance/object should have since, as
# mentioned, classes are the blueprints that contain attributes and methods
# for each instance/object
# To do this, we use the self parameter which represents each specific
# individual instance/object of a class every time you instantiate a new
# instance of a class which allows each instance/object to have their own
# attributes and methods and also allows access to the attributes and methods
# of each instance/object
class User:
    # Typically, you name the attribute the same name as the corresponding
    # parameter
    # As mentioned, the attributes and methods are also known as instance
    # attributes and instance methods since they are defined to each
    # individual instance/object
    # Instance methods that ONLY retrieve and return (get) attributes are
    # known as getters
    # Instance methods that ONLY pass in (set) attributes once and don't
    # return or change/update attributes are known as setters
    def __init__(self, first_name: str, last_name: str, age: int):
        # Instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Instance method (getter)
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # Instance method (getter)
    def initials(self) -> str:
        return f"{self.first_name[0]}.{self.last_name[0]}."

    # Instance method (getter)
    def food_likes(self, food: str) -> str:
        return f"{self.first_name} likes {food}"

    # Instance method (getter)
    def is_senior(self) -> bool:
        return self.age >= 65

    # Instance method (not a getter or setter)
    # This method shows that instance attributes are dynamic not static since
    # they can be changed/updated
    # However this is not a getter or setter since getters ONLY return data
    # and setters ONLY set data - This method does not only return data so it's
    # not considered a true getter and because it returns and changes/updates
    # data it's not considered a true setter since setters don't return data
    # and they don't change/update data, they are used to just pass it in to
    # set once not to return or change/update the data after it has already
    # been set (Validation logic and error catching/handling is often used in
    # setters to make sure the data is set correctly the first time)
    def happy_birthday(self) -> str:
        self.age += 1
        return f"Happy {self.age} birthday, {self.first_name}!"


# Similar to functions, you must pass in the same number of arguments to the
# method otherwise Python will raise an error unless you have defaults set up
# in your signature - The self parameter must always be used as the first
# parameter when we define methods however you don’t ever pass anything into
# the self parameter and instead whatever you pass in first will be passed
# in to the second parameter
# Remember that the below is also how you instantiate a class since you need to
# create an instance/object of the class except now we are actually passing in
# arguments since our User class is no longer empty
# Anytime we create a new instance of a class, Python will look for the
# __init__ dunder method inside the class and then the arguments will be
# automatically passed in to the __init__ dunder method to set and initialize
# the data (attributes) that each User instance/object should have
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

# Then to access specific instance attributes on an instance/object, you can
# use the . dot operator and run:
# print(instance_name.instance_attribute_name)
print(user1.first_name)
print(user1.first_name, user1.last_name)
print(user2.first_name, user2.last_name)
print("")

# You can also call the following methods created above on an instance/object
# to easily get their data
print(user1.full_name())
print(user2.full_name())
print(user1.initials())
print(user2.initials())
print(user1.food_likes("ice cream"))
print(user2.food_likes("chocolate"))
print(user1.is_senior())
print(user2.is_senior())
print("")

# The happy_birthday() method changes/updates the age instance attribute when
# you call it on an instance/object
print(user1.age)
print(user1.happy_birthday())
print(user1.age)
print(user2.age)
print(user2.happy_birthday())
print(user2.age)
