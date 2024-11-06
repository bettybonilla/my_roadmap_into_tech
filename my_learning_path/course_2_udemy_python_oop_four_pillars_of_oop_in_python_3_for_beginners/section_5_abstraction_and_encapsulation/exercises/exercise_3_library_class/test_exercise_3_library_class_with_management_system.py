from dataclasses import dataclass


@dataclass
class _BookInformation:
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
    def get_book_collection() -> dict[str, list[_BookInformation]]:
        return {key: value for key, value in Library._book_collection.items()}

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


# This class is not unit testable since these methods use the input() function
# to pass in data therefore, it's bad practice to do this for this reason
class Customer:
    def __init__(self):
        self.book = None

    def request_book(self) -> str:
        self.book = input()
        return self.book

    def return_book(self) -> str:
        self.book = input()
        return self.book


def user_action(library: Library, customer: Customer, user_choice: int) -> bool:
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
        case _:
            print("\nPlease enter a valid choice!\n")
            return False
    return True


def application_logic():
    library = Library()
    customer = Customer()

    while True:
        print("Welcome!\n")
        print("Enter 1 to display the available books")
        print("Enter 2 to request a book")
        print("Enter 3 to return a book")
        print("Enter 4 to exit\n")
        user_choice = int(input())
        # Since this choice exits/quits the program it is not unit testable and
        # it's why it's not a match-case statement in the user_action function
        # since all of those match-case statements are unit testable
        if user_choice == 4:
            quit(0)

        # An _ underscore is used as a variable when the return of a function
        # is not going to be used since typically you would save the return of
        # a function to a variable and use it to do something with it but in
        # this case this function just needs to be called
        _ = user_action(library, customer, user_choice)


if __name__ == "__main__":
    # This is commented out so that it doesn't run during testing
    # application_logic()

    import io
    import sys
    import unittest

    # When you run unit tests, the methods that you created in your unit test
    # class are tested randomly therefore if you are trying to test things in
    # a particular order you need to have all your tests in one method instead
    # of separate methods - Typically, you should have your methods randomly
    # tested in your unit test class so therefore you should create separate
    # methods which would contain tests for each method you want to test
    class TestLibrary(unittest.TestCase):
        def test_methods(self):
            # This is used to remove print statements from your terminal when
            # you run unit tests
            # The stdout stands for standard out and it is what is printed to
            # your terminal
            # All the strings printed to terminal are being saved to the
            # suppress_text variable which is how they're removed from
            # terminal when you run your unit tests
            # This is applied due to the last unit test for invalid input
            # which otherwise would have printed "Please enter a valid choice!"
            suppress_text = io.StringIO()
            sys.stdout = suppress_text

            library = Library()
            customer = Customer()
            author = "Stephenie Meyer"
            twilight_index = 0
            new_moon_index = 1
            gibberish = "asdf"

            # Test lend_book
            # Twilight
            self.assertEqual(
                library._book_collection[author][twilight_index].number_of_copies,
                1,
                msg="Should start with 1 copy",
            )
            self.assertTrue(library.lend_book("Twilight"))
            self.assertEqual(
                library._book_collection[author][twilight_index].number_of_copies,
                0,
                msg="Should go to 0, from 1",
            )
            self.assertFalse(library.lend_book("Twilight"))
            self.assertEqual(
                library._book_collection[author][twilight_index].number_of_copies,
                0,
                msg="Should not go below 0",
            )

            # New Moon
            self.assertEqual(
                library._book_collection[author][new_moon_index].number_of_copies,
                1,
                msg="Should start with 1 copy",
            )
            self.assertTrue(library.lend_book("New Moon"))
            self.assertEqual(
                library._book_collection[author][new_moon_index].number_of_copies,
                0,
                msg="Should go to 0, from 1",
            )
            self.assertFalse(library.lend_book("New Moon"))
            self.assertEqual(
                library._book_collection[author][new_moon_index].number_of_copies,
                0,
                msg="Should not go below 0",
            )

            # Gibberish
            self.assertFalse(library.lend_book(gibberish))

            # Test add_book
            # Twilight
            self.assertEqual(
                library._book_collection[author][twilight_index].number_of_copies,
                0,
                msg="Should have 0 copies now",
            )
            self.assertTrue(library.add_book("Twilight"))
            self.assertEqual(
                library._book_collection[author][twilight_index].number_of_copies,
                1,
                msg="Should go to 1, from 0",
            )

            # New Moon
            self.assertEqual(
                library._book_collection[author][new_moon_index].number_of_copies,
                0,
                msg="Should have 0 copies now",
            )
            self.assertTrue(library.add_book("New Moon"))
            self.assertEqual(
                library._book_collection[author][new_moon_index].number_of_copies,
                1,
                msg="Should go to 1, from 0",
            )

            # Gibberish
            self.assertFalse(library.add_book(gibberish))

            # Invalid input
            self.assertFalse(user_action(library, customer, user_choice=5))

    unittest.main()
