"""
Implement a library management system which will handle the following tasks:
- Customer should be able to display all the books available in the library
- Handle the process when a customer requests to borrow a book
- Update the library collection when the customer returns a book
"""


class Library:
    _book_collection = {
        "Stephenie Meyer": ["Twilight", "New Moon", "Eclipse", "Breaking Dawn"]
    }

    @staticmethod
    def borrow_book(author: str, book_title: str):
        author_found = Library._book_collection.get(author)
        if author_found:
            author_found.remove(book_title)

    @staticmethod
    def return_book(author: str, book_title: str):
        author_found = Library._book_collection.get(author)
        if author_found:
            author_found.append(book_title)

    # As mentioned, using get vs. display is a method naming convention that
    # implies how your method should behave and retrieve data so that the
    # reader of your code knows what to expect - This applies to instance
    # methods, static methods, etc.
    # get - Should use a return statement which requires the method call to be
    # wrapped in a print statement
    # display - Should use a print statement which doesn’t require the method
    # call to be wrapped in a print statement therefore you can just do the
    # method call
    @staticmethod
    def get_book_collection() -> dict[str, list[str]]:
        return {key: value for key, value in Library._book_collection.items()}


customer1 = Library()
print(customer1.get_book_collection())
customer1.borrow_book("Stephenie Meyer", "Twilight")
print(customer1.get_book_collection())
customer1.return_book("Stephenie Meyer", "Twilight")
print(customer1.get_book_collection())
