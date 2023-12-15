"""
Below we've added class methods to the User class
"""


# Just like class attributes, a class method is not concerned with
# instances/objects but the class itself and can be defined with the
# @classmethod decorator right above it
# Class methods can be used when you don’t need access to a particular
# instance/object of a class or their instance/class attributes but when you
# want to create a new instance of a class or validate data before the
# instance/object is created (which is different from validating a specific
# instance attribute)
class User:
    # Public class attribute
    # As mentioned, class attributes are defined once and go at the very top
    # of a class typically above the __init__ dunder method
    active_users = 0

    def __init__(self, first_name: str, last_name: str, age: int):
        # Initialized all instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # Anytime a new User instance/object is created, it will update the
        # active_users class attribute by incrementing it by 1
        User.active_users += 1

    # Class method (getter)
    # As mentioned, there’s no particular place you should define class
    # methods however just make sure you’re consistent
    # With class methods, the class will be automatically passed into the
    # class method when you call it so the standard parameter name most
    # commonly used is cls, which stands for class, instead of using the self
    # parameter - Instance methods use the self parameter since
    # instances/objects are automatically passed into instance methods
    @classmethod
    def get_active_users(cls) -> str:
        # The cls parameter is the class User not an instance/object of User
        # As we can see, when we call this class method and it prints the cls
        # parameter, it prints <class '__main__.User'> however it does not
        # print the memory address of the object since it's not an
        # instance/object of User
        print(cls)
        # Using cls.active_users is bad practice since you shouldn't use class
        # methods to access class attributes
        # Class methods are meant to be used to access the built-in’s offered
        # for all classes (found in the builtins.pyi file by stepping into
        # object when passed into any class signature) NOT to access the class
        # attributes you’ve defined
        return f"There are currently {cls.active_users} active users"

    # Class method (setter)
    # When this class method is called, it can be used to create a new
    # instance of the User class by taking in one string that has the
    # arguments required for a User instance/object, splitting it, and then it
    # will return the new User instance/object which will be passed into the
    # __init__ dunder method to be set and initialized
    @classmethod
    def from_string(cls, data_str: str):
        # Assigns the 3 variables (first, last, age) at once to the string
        # being passed in for the data_str parameter which will be split with
        # a comma using the .split() method so that it can be assinged to each
        # of the 3 corresponding variables (first, last, age)
        first, last, age = data_str.split(",")
        age = int(age)
        # This will be the same as instantiating an instance/object using
        # User(first_name, last_name, age) which will automatically run the
        # __init__ dunder method above since, as mentioned, the cls parameter
        # is the class User and anytime we create a new instance of a class
        # the arguments will be automatically passed into the __init__ dunder
        # method to set and initialize the data (attributes) for the new User
        # instance/object
        return cls(first, last, age)

    # Instance method (not a getter or setter)
    # Changes/updates the active_users class attribute by decrementing it by 1
    # when you call it on an instance/object
    def log_out(self) -> str:
        User.active_users -= 1
        return f"{self.first_name} has logged out"

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
    def happy_birthday(self) -> str:
        self.age += 1
        return f"Happy {self.age} birthday, {self.first_name}!"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

# To access specific class methods on a class, you can use the . dot
# operator and run:
# print(class_name.class_method_name())
print(User.get_active_users())

# Instantiates a new User using the from_string class method above
user3 = User.from_string("Tom, Jones, 89")
print(user3.first_name, user3.last_name, user3.age)
print(user3.full_name())
print(User.get_active_users())
print(user3.is_senior())
print(user3.happy_birthday())
