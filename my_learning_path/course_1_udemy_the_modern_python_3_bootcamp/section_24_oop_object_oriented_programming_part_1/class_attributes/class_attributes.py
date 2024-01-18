"""
Below we've added a class attribute to the User class
"""


# A class attribute is defined once and it lives in the class itself and is
# shared with all instances/objects of a class and the class itself
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


# To access specific class attributes on a class, you can use the . dot
# operator and run:
# print(class_name.class_attribute_name)
print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users)
print(user2.log_out())
print(User.active_users)
