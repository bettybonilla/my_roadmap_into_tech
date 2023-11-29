"""
Write an object-oriented program that performs the following tasks:
- Create a class called Chair from the base class Furniture
- Teakwood should be the type of wood that is used by all Furniture classes by
default
- The user can be given an option to change the type of wood used for Chair if
he wishes to
- The number of legs of a Chair should be a property that should not be
altered outside the class
"""


class Furniture:
    _type_of_wood = "Teakwood"


class Chair(Furniture):
    __number_of_legs = 4

    def __init__(self):
        self.type_of_wood = None
        self.set_type_of_wood()

    def set_type_of_wood(self, user_wood_choice: str = Furniture._type_of_wood) -> bool:
        if user_wood_choice:
            self.type_of_wood = user_wood_choice
            return True
        return False

    def display_specifications(self):
        print("\nChair Specifications\n")
        print(f"Type of Wood: {self.type_of_wood}")
        print(f"Number of Legs: {self._Chair__number_of_legs}\n")


chair1 = Chair()

while True:
    print("Enter 1 to display the specifications of your chair")
    print("Enter 2 to change the type of wood of your chair")
    print("Enter 3 to exit\n")

    user = int(input())

    match user:
        case 1:
            chair1.display_specifications()
        case 2:
            print("\nThe default type of wood is Teakwood\n")
            print("Press enter to keep the default (Teakwood)\n")
            print("Or enter your desired type of wood\n")
            user_wood_choice = input()
            if chair1.set_type_of_wood(user_wood_choice):
                print(
                    f"\nThe type of wood of your chair has been changed to {user_wood_choice}\n"
                )
            else:
                print(
                    "The type of wood of your chair will remain the default (Teakwood)\n"
                )
        case 3:
            exit(0)
        case _:
            print("\nPlease enter a valid choice!\n")
