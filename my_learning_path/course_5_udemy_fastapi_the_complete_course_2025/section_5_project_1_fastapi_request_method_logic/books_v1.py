"""
Create and enhance books to learn the basics of FastAPI using CRUD (Create, Read, Update, Delete) operations
"""

from typing import Optional

from fastapi import FastAPI, Body

# The if __name__ == "__main__" statement is not used so that the app variable is not indented within this if statement
# since it needs to be globally scoped and directly accessible when you run this file in terminal - For this reason,
# this is why app = FastAPI() should be in its own main.py file
app = FastAPI()


# This is considered a GET HTTP request method since it can read and get data to return as a response back to the client
# However the @app.get() decorator needs to be added above the function along with passing in the specified API endpoint
# which will call this function - The specified API endpoint can be named according to what it will return as a response
# back to the client
# When you start your FastAPI application (backend server), FastAPI will spin up all API endpoints - This is called
# spinning up your server :-)
# To start your FastAPI application (backend server) and spin up your server, you must run this file in terminal using
# the following command:
# uvicorn books_v1:app --reload
# - uvicorn is the web server that comes installed with FastAPI which is used to start a FastAPI application
# (backend server)
# - books_v1 is the Python file we're referring to
# - app is the app variable in your Python file which is assigned to FastAPI
# - --reload will allow your FastAPI application (backend server) to reload everytime there's a code change
# To kill your server, press CTRL + C
# In FastAPI, if a function is asynchronous FastAPI will add the async functionality in the background even if the async
# keyword is not used however you should ALWAYS use the async keyword explicitly with ALL your functions no matter what
# they do since you need it in order for ALL your functions to run smoothly and asynchronously with each other
# The async keyword is essential to any backend server however it colors your functions - Colored functions will only be
# able to call other colored functions using the same keyword so this is why it’s important to use the async keyword
# explicitly with ALL your functions to avoid any issues
# URL: 127.0.0.1:8000/api-endpoint
# - 127.0.0.1 is your local host
# - 8000 is the port
@app.get("/api-endpoint")
async def first_api() -> dict[str, str]:
    return {"message": "Hello Eric!"}


BOOKS = [
    {"title": "Title_One", "author": "Author_One", "category": "science"},
    {"title": "Title_Two", "author": "Author_Two", "category": "science"},
    {"title": "Title_Three", "author": "Author_Three", "category": "history"},
    {"title": "Title_Four", "author": "Author_Four", "category": "math"},
    {"title": "Title_Five", "author": "Author_Five", "category": "math"},
    {"title": "Title_Six", "author": "Author_Two", "category": "math"},
]


# As mentioned, the specified API endpoint can be named according to what it will return as a response back to the
# client
# The API endpoint below is a static path since it has been hard coded and the function does not have path parameters in
# its decorator to take in request arguments from the client to change its path
# This function returns all books as a response back to the client
# URL: 127.0.0.1:8000/books
@app.get("/books")
async def read_all_books() -> list[dict[str, str]]:
    return BOOKS


# The API endpoint below is a dynamic path since the function has a path parameter in its decorator to take in a request
# argument from the client to change its path
# This function returns the book with the specific book title as a response back to the client
# URL: 127.0.0.1:8000/books/{book_title}
@app.get("/books/{book_title}")
async def read_book(book_title: str) -> Optional[dict[str, str]]:
    for book in BOOKS:
        # The .casefold() method is a more aggressive string method than the .lower() method since it can convert
        # special characters outside the ASCII characters to lowercase
        if book.get("title").casefold() == book_title.casefold():
            return book


# The API endpoint below is a static path and it is using a query parameter in its function to take in a request keyword
# argument from the client as a query argument to return a filtered response of all books from a specific category back
# to the client
# URL: 127.0.0.1:8000/books/q/
@app.get("/books/q/")
async def read_category_by_query(category: str) -> Optional[list[dict[str, str]]]:
    book_list = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            book_list.append(book)
    if not book_list:
        return None
    return book_list


# The API endpoint below is a static path and it is using a query parameter in its function to take in a request keyword
# argument from the client as a query argument to return a filtered response of all books from a specific author back to
# the client
# URL: 127.0.0.1:8000/books/author/q/
@app.get("/books/author/q/")
def read_author_by_query(author: str) -> Optional[list[dict[str, str]]]:
    book_list = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            book_list.append(book)
    if not book_list:
        return None
    return book_list


# The API endpoint below is a dynamic path and it is using a path parameter and a query parameter in its function to
# take in a request argument to change its path and to take in a request keyword argument from the client as a query
# argument to return a filtered response of all books from a specific author and a specific category back to the client
# URL: 127.0.0.1:8000/books/{book_author}/q/
@app.get("/books/{book_author}/q/")
async def read_author_category_by_query(
    book_author: str, category: str
) -> Optional[list[dict[str, str]]]:
    book_list = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            book_list.append(book)
    if not book_list:
        return None
    return book_list


# The API endpoint below is a static path and its function will take in a request body from the client to create data
# URL: 127.0.0.1:8000/books/create-book
@app.post("/books/create-book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


# The API endpoint below is a static path and its function will take in a request body from the client to update data
# URL: 127.0.0.1:8000/books/update-book
@app.put("/books/update-book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


# The API endpoint below is a dynamic path since the function has a path parameter in its decorator to take in a request
# argument from the client to change its path and delete data
# URL: 127.0.0.1:8000/books/delete-book/{book_title}
@app.delete("/books/delete-book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
