# Class: Library
# Layers of abstraction: display available books, lend a book, add a book

# Class: Customer
# Layers of abstraction: request a book, return a book


class Library:
    def __init__(self, available_books: list[str]):
        self.available_books = available_books

    def display_available_books(self):
        print("\nAvailable Books:\n")
        for book in self.available_books:
            print(book)
        print("")

    def lend_book(self, requested_book: str):
        if requested_book in self.available_books:
            print("\nYou have borrowed the book. Happy reading!\n")
            self.available_books.remove(requested_book)
        else:
            print("\nSorry that book is not available\n")

    def add_book(self, returned_book: str):
        self.available_books.append(returned_book)
        print("\nYou have returned the book. Thank you!\n")


class Customer:
    def request_book(self) -> str:
        print("\nEnter the name of the book you would like to borrow:")
        self.book = input()
        return self.book

    def return_book(self) -> str:
        print("\nEnter the name of the book you would like to return:")
        self.book = input()
        return self.book


library = Library(
    ["Think and Grow Rich", "Who Will Cry When You Die", "For One More Day"]
)
customer = Customer()

print("Welcome!\n")

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit\n")

    user_choice = int(input())

    if user_choice == 1:
        library.display_available_books()
    elif user_choice == 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice == 3:
        returned_book = customer.return_book()
        library.add_book(returned_book)
    elif user_choice == 4:
        quit()
