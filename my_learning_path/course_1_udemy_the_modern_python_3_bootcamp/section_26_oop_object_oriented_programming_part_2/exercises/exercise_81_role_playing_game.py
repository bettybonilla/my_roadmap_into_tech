"""
Let's pretend we're building an RPG (Role Playing Game) in Python!
- Define a base parent class called Character that has the following
attributes:
    - name - string
    - hp - integer value representing health (AKA hit points)
    - level - integer value representing experience level
- Define a subclass child class called NPC (Non-Player Character)
that inherits from Character, and has an additional instance method called
speak which prints the speech that character would say when a player interacts
with them
- Ex:
    villager = NPC("Bob", 100, 12)
    villager.name  # Bob
    villager.hp  # 100
    villager.level  # 12
    villager.speak()  # "I heard there were monsters running around last
    night!"
"""


# Base parent class
class Character:
    def __init__(self, name: str, hp: int, level: int):
        self.name = name
        self.hp = hp
        self.level = level


# Subclass child class
class NPC(Character):
    def __init__(self, name: str, hp: int, level: int):
        super().__init__(name, hp, level)

    def speak(self) -> str:
        return "I heard there were monsters running around last night!"


villager = NPC("Bob", 100, 12)
print(villager.name)
print(villager.hp)
print(villager.level)
print(villager.speak())
