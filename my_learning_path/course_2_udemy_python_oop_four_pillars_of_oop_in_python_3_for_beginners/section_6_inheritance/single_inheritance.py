"""
The below shows single inheritance
"""


# Base parent class
class Apple:
    manufacturer = "Apple, Inc."
    contact_website = "www.apple.com/contact"

    @staticmethod
    def display_contact_details():
        print(f"To contact us, log on to {Apple.contact_website}")


# Subclass child class AKA derived class
class MacBook(Apple):
    def __init__(self):
        self.year_of_manufacture = 2017

    def display_manufacture_details(self):
        print(
            f"This MacBook was manufactured in the year {self.year_of_manufacture} by {self.manufacturer}"
        )


mac = MacBook()
mac.display_contact_details()
mac.display_manufacture_details()
