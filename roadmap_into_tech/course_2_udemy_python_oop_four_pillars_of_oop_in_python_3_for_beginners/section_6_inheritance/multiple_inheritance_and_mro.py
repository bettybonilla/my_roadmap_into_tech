"""
The below shows multiple inheritance and MRO (Method Resolution Order)
"""


# Base parent class
class OperatingSystem:
    multitasking = True
    name = "Mac OS"


# Base parent class
class Apple:
    website = "www.apple.com"
    name = "Apple"


# Subclass child class AKA derived class
class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking:
            print(
                f"This is a multi-tasking system. Visit {self.website} for more details."
            )
            # Only prints the name class attribute from the OperatingSystem
            # base parent class due to MRO (Method Resolution Order)
            print(f"Name: {self.name}")


mac = MacBook()
