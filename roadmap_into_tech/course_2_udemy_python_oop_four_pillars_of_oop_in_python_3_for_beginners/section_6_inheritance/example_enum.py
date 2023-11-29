from enum import Enum


class Wood(Enum):
    DARK = 0
    LIGHT = 1

    def __str__(self) -> str:
        return self.name

    @classmethod
    def display_wood_choice(cls):
        print("Enter your choice to select wood type:")
        for item in [(e.name, e.value) for e in cls]:
            print(f"{item[1]} -> {item[0]}")


Wood.display_wood_choice()
user_choice = int(input())
print(Wood(user_choice))

# References
# https://www.geeksforgeeks.org/classmethod-in-python/#:~:text=In%20general%2C%20static%20methods%20know%20nothing%20about%20the%20class%20state.%20They%20are%20utility%2Dtype%20methods%20that%20take%20some%20parameters%20and%20work%20upon%20those%20parameters.%20On%20the%20other%20hand%20class%20methods%20must%20have%20class%20as%20a%20parameter.
