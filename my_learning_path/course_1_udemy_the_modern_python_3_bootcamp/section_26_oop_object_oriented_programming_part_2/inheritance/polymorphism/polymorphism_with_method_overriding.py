"""
The below shows polymorphism by using method overriding
"""


# Base parent class
class Animal:
    def speak(self):
        # Raises the NotImplementedError to notify any other subclass child
        # class that's inheriting from this base parent class that it needs to
        # have its own implementation
        raise NotImplementedError(
            "Subclass needs to have its own implementation of this instance method"
        )


# Subclass child class
# Hierarchical inheritance
class Cat(Animal):
    # Method overrides with its own implementation
    def speak(self) -> str:
        return "meow"


# Subclass child class
# Hierarchical inheritance
class Dog(Animal):
    # Method overrides with its own implementation
    def speak(self) -> str:
        return "woof"


# Subclass child class
# Hierarchical inheritance
class Human(Animal):
    pass


c = Cat()
print(c.speak())
d = Dog()
print(d.speak())
h = Human()
# Since this subclass child class inherits from the Animal base parent class
# but does not method override the speak instance method with its own
# implementation, it raises the NotImplementedError
print(h.speak())
