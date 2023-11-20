"""
Below we've added the Moderator subclass child class and used the super()
function for single inheritance
"""


# Base parent class
class User:
    active_users = 0

    def __init__(self, first_name: str, last_name: str, age: int):
        # Initialized all instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        User.active_users += 1

    # Class method (getter)
    @classmethod
    def get_active_users(cls) -> str:
        return f"There are currently {cls.active_users} active users"

    # Class method (setter)
    @classmethod
    def from_string(cls, data_str: str):
        first, last, age = data_str.split(",")
        age = int(age)
        return cls(first, last, age)

    # Instance method (not a getter or setter)
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


# Subclass child class
# Moderators are still users however they have privileges regular users do not
# have to help manage communities on social media platforms like Reddit, etc.
class Moderator(User):
    active_mods = 0

    def __init__(self, first_name: str, last_name: str, age: int, community: str):
        # Initialized all instance attributes
        super().__init__(first_name, last_name, age)
        self.community = community
        Moderator.active_mods += 1

    # Class method (getter)
    @classmethod
    def get_active_mods(cls) -> str:
        return f"There are currently {cls.active_mods} active moderators"

    def remove_post(self) -> str:
        return f"{self.full_name()} removed a post from the {self.community} community"


# Since the Moderator subclass child class is inheriting from the User base
# parent class, it inherits everything from the User base parent class
# including the active_users class attribute and User.active_users += 1 in the
# __init__ dunder method
print(User.get_active_users())
mod1 = Moderator("Jasmine", "O'Connor", 61, "Piano")
print(mod1.full_name())
print(mod1.community)
print(User.get_active_users())
user1 = User("Tom", "Garcia", 35)
print(User.get_active_users())
print("")

user2 = User("Tom", "Garcia", 35)
user3 = User("Tom", "Garcia", 35)
mod2 = Moderator("Jasmine", "O'Connor", 61, "Piano")
print(User.get_active_users())
print(Moderator.get_active_mods())
