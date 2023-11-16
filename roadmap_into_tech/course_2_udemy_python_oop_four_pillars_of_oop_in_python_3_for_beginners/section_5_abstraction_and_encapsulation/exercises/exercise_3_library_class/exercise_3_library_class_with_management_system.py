from dataclasses import dataclass


@dataclass
class _BookInformation:
    title = str
    number_of_copies = int

    def __init__(self, title: str, number_of_copies: int):
        self.title = title
        self.number_of_copies = number_of_copies

    def __repr__(self) -> str:
        return f"{self.title}: {self.number_of_copies}"


class Library:
    _book_collection = {
        "Stephenie Meyer": [
            _BookInformation("Twilight", 1),
            _BookInformation("New Moon", 1),
            _BookInformation("Eclipse", 1),
            _BookInformation("Breaking Dawn", 1),
        ]
    }

    @staticmethod
    def lend_book(requested_book: str) -> bool:
        for value in Library._book_collection.values():
            for i in value:
                if requested_book == i.title and i.number_of_copies > 0:
                    i.number_of_copies -= 1
                    return True
        return False

    @staticmethod
    def add_book(returned_book: str) -> bool:
        for value in Library._book_collection.values():
            for i in value:
                if returned_book == i.title:
                    i.number_of_copies += 1
                    return True
        return False

    @staticmethod
    def get_book_collection() -> dict[str, list[_BookInformation]]:
        return {key: value for key, value in Library._book_collection.items()}


class Customer:
    def __init__(self):
        self.book = None

    def request_book(self) -> str:
        self.book = input()
        return self.book

    def return_book(self) -> str:
        self.book = input()
        return self.book


# The below would be application logic and it's where all your print
# statements should live especially ones containing strings
# It's good practice to return a boolean value in your methods instead of
# returning strings since if you need to change/update your strings, it will be
# easier to change/update them in the application logic so you don't have to
# touch your method logic - Users would also just be able to make the
# changes/updates in the application logic instead of having to wait for you
# to release an update to your method logic
library = Library()
customer = Customer()

print("Welcome!\n")

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit\n")

    user_choice = int(input())

    # Using match-case statements
    match user_choice:
        case 1:
            print("\nAvailable Books:\n")
            print(library.get_book_collection())
            print("")
        case 2:
            print("\nEnter the name of the book you would like to borrow:")
            requested_book = customer.request_book()
            if library.lend_book(requested_book):
                print("\nYou have borrowed the book. Happy reading!\n")
            else:
                print("\nSorry that book is not available\n")
        case 3:
            print("\nEnter the name of the book you would like to return:")
            returned_book = customer.return_book()
            if library.add_book(returned_book):
                print("\nYou have returned the book. Thank you!\n")
            else:
                print("")
        case 4:
            quit(0)
        case _:
            print("\nPlease enter a valid choice!\n")

    # Alternative code using if statements
    # if user_choice == 1:
    #     print("\nAvailable Books:\n")
    #     print(library.get_book_collection())
    #     print("")
    # elif user_choice == 2:
    #     print("\nEnter the name of the book you would like to borrow:")
    #     requested_book = customer.request_book()
    #     if library.lend_book(requested_book):
    #         print("\nYou have borrowed the book. Happy reading!\n")
    #     else:
    #         print("\nSorry that book is not available\n")
    # elif user_choice == 3:
    #     print("\nEnter the name of the book you would like to return:")
    #     returned_book = customer.return_book()
    #     if library.add_book(returned_book):
    #         print("\nYou have returned the book. Thank you!\n")
    #     else:
    #         print("")
    # elif user_choice == 4:
    #     quit(0)
    # else:
    #     print("\nPlease enter a valid choice!\n")
