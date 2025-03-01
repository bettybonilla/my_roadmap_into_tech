"""
The below shows how we can use the super() function for multiple inheritance
which allows a subclass child class to inherit from more than one base parent
class
- MRO (Method Resolution Order) is also displayed below
"""


# Base parent class
class Aquatic:
    def __init__(self, name: str):
        self.name = name

    def swim(self) -> str:
        return f"{self.name} can swim"

    def greet(self) -> str:
        return f"I am {self.name} from the sea!"


# Base parent class
class Ambulatory:
    def __init__(self, name: str):
        self.name = name

    def walk(self) -> str:
        return f"{self.name} can walk"

    def greet(self) -> str:
        return f"I am {self.name} from the land!"


# Subclass child class
class Penguin(Aquatic, Ambulatory):
    def __init__(self, name: str):
        super().__init__(name)
        # Instead of using the super() function, you can also manually call
        # each base parent class that the subclass child class is inheriting
        # from in its signature however you have to provide the self parameter
        # Aquatic.__init__(self, name)
        # Ambulatory.__init__(self, name)


nemo = Aquatic("Nemo")
hachi = Ambulatory("Hachi")
piplup = Penguin("Piplup")
print(piplup.swim())
print(piplup.walk())
# Due to MRO (Method Resolution Order), since both base parent classes contain
# the greet instance method, the greet instance method inside the first base
# parent class passed in the subclass child class signature will be called
# first since this is how Python decides between which method to call first
# when they share the same method name
# Therefore, the Aquatic greet instance method is called first and returns "I
# am Piplup from the sea!"
print(piplup.greet())
print("")

print(f"Piplup is an instance of Aquatic: {isinstance(piplup, Aquatic)}")
print(f"Piplup is an instance of Ambulatory: {isinstance(piplup, Ambulatory)}")
print(f"Piplup is an instance of Penguin: {isinstance(piplup, Penguin)}")
