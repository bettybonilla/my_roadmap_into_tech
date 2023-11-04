"""
The below shows some different ways you can find out the MRO (Method
Resolution Order) of a class
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

# Some different ways you can find out the MRO (Method Resolution Order) of a
# class:
# Using the __mro__ attribute
print(Penguin.__mro__)
print("")
# Using the .mro() method
print(Penguin.mro())
print("")
# Using the help() function
# This option gives the most detailed readable format
print(help(Penguin))
