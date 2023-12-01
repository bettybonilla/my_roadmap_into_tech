from enum import Enum


# Because Enums are used to represent constants, it is strongly recommended to
# use UPPER_CASE names for members
class Wood(Enum):
    TEAKWOOD = 0
    MAPLE = 1
    BIRCH = 2
    WHITE_OAK = 3
    WALNUT = 4

    def __str__(self) -> str:
        return self.name

    @classmethod
    def display_wood_choice(cls):
        for item in [(e.name, e.value) for e in cls]:
            print(f"{item[1]} -> {item[0]}")


class Furniture:
    _type_of_wood = Wood(0)


class Chair(Furniture):
    __number_of_legs = 4

    def __init__(self):
        self.type_of_wood = None
        self.set_type_of_wood()

    def set_type_of_wood(self, user_wood_choice: str = Furniture._type_of_wood) -> bool:
        if user_wood_choice:
            self.type_of_wood = Wood(user_wood_choice)
            return True
        return False

    def display_specifications(self):
        print(f"Type of Wood: {self.type_of_wood}")
        print(f"Number of Legs: {self._Chair__number_of_legs}")


chair1 = Chair()

while True:
    print("Enter 1 to display the specifications of your chair")
    print("Enter 2 to change the type of wood of your chair")
    print("Enter 3 to exit\n")

    user = int(input())

    match user:
        case 1:
            print("\nChair Specifications\n")
            chair1.display_specifications()
            print("")
        case 2:
            print(f"\nThe default type of wood is {Wood(0)}\n")
            print("Enter your choice to select type of wood\n")
            Wood.display_wood_choice()
            print("")
            user_wood_choice = int(input())
            if chair1.set_type_of_wood(user_wood_choice):
                print(
                    f"\nThe type of wood of your chair has been changed to {Wood(user_wood_choice)}\n"
                )
            else:
                print(
                    f"\nThe type of wood of your chair will remain the default ({Wood(0)})\n"
                )
        case 3:
            exit(0)
        case _:
            print("\nPlease enter a valid choice!\n")
