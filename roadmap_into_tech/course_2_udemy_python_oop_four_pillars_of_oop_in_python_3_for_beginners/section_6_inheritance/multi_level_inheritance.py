"""
The below shows multi-level inheritance
"""


# Base parent class
class MusicalInstrument:
    number_of_major_keys = 12


# Intermediary subclass child class
class StringInstrument(MusicalInstrument):
    type_of_wood = "Tonewood"


# Subclass child class AKA derived class
class Guitar(StringInstrument):
    def __init__(self):
        self.number_of_strings = 6
        print(
            f"This guitar consists of {self.number_of_strings} strings. It is made of {self.type_of_wood} and it can play {self.number_of_major_keys} keys."
        )


g = Guitar()
