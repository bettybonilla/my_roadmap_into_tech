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
    def get_book_collection() -> dict[str, list[_BookInformation]]:
        return {key: value for key, value in Library._book_collection.items()}

    @staticmethod
    def borrow_book(author: str, book_title: str):
        author_found = Library._book_collection.get(author)
        if author_found:
            for i in author_found:
                if i.title == book_title and i.number_of_copies > 0:
                    i.number_of_copies -= 1

    @staticmethod
    def return_book(author: str, book_title: str):
        author_found = Library._book_collection.get(author)
        if author_found:
            for i in author_found:
                if i.title == book_title:
                    i.number_of_copies += 1


customer1 = Library()
print(customer1.get_book_collection())
customer1.borrow_book("Stephenie Meyer", "Twilight")
print(customer1.get_book_collection())
customer1.borrow_book("Stephenie Meyer", "Twilight")
print(customer1.get_book_collection())
customer1.borrow_book("Stephenie Meyer", "New Moon")
print(customer1.get_book_collection())
customer1.return_book("Stephenie Meyer", "Twilight")
print(customer1.get_book_collection())
customer1.return_book("Stephenie Meyer", "New Moon")
print(customer1.get_book_collection())
