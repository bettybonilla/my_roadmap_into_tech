"""
Continue to enhance books using CRUD (Create, Read, Update, Delete) operations along with data validation, Python
request objects, swagger configuration, exception handling, and status codes
"""

from typing import Optional, NoReturn

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

# BOOKS = []


# The typing.NoReturn module is not a valid Pydantic field type
# In order to use this type annotation, you must use the response_model=None path operation decorator parameter
# https://docs.pydantic.dev/1.10/usage/types/
# https://fastapi.tiangolo.com/tutorial/response-model/
# @app.get("/books", response_model=None)
# async def read_all_books() -> list[NoReturn]:
#     return BOOKS


class Book:
    def __init__(
        self,
        id: int,
        title: str,
        author: str,
        description: str,
        rating: int,
        published_date: int,
    ):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    # Pydantic v2 requires Optional[] = None explicitly for this type annotation
    # id: Optional[int] = None
    # The code above has been refactored to the code below
    # A description can be added to clarify our variables but, as mentioned above, the default needs to be explicit
    id: Optional[int] = Field(description="id is not required on create", default=None)
    # title needs to be a str of a minimum of 3 characters
    title: str = Field(min_length=3)
    # author needs to be a str of a minimum of 1 character
    author: str = Field(min_length=1)
    # description needs to be a str of a minimum of 1 character and a maximum of 100 characters
    description: str = Field(min_length=1, max_length=100)
    # rating needs to be an int greater than 0 and less than 6 (Ex: 1-5)
    rating: int = Field(gt=0, lt=6)
    # published_date needs to be an int greater than 1999 and less than 2026 (Ex: 2000-2025)
    published_date: int = Field(gt=1999, lt=2026)

    # Pydantic v2 converted Config class to model_config
    # Pydantic v2 renamed schema_extra to json_schema_extra
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A New Book",
                "author": "codingwithroby",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2012,
            }
        }
    }


BOOKS = [
    Book(1, "Computer Science Pro", "codingwithroby", "A very nice book!", 5, 2012),
    Book(2, "Be Fast With FastAPI", "codingwithroby", "A great book!", 5, 2012),
    Book(3, "Master Endpoints", "codingwithroby", "An awesome book!", 5, 2014),
    Book(4, "HP1", "author1", "Book description", 2, 2001),
    Book(5, "HP2", "author2", "Book description", 3, 2002),
    Book(6, "HP3", "author3", "Book description", 1, 2003),
]


@app.get("/books", response_model=None, status_code=status.HTTP_200_OK)
async def read_all_books() -> list[Book]:
    return BOOKS


@app.get("/books/{book_id}", response_model=None, status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)) -> Optional[Book]:
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/books/q/", response_model=None, status_code=status.HTTP_200_OK)
async def read_book_by_rating(
    book_rating: int = Query(gt=0, lt=6)
) -> list[Book | NoReturn]:
    book_list = []
    for book in BOOKS:
        if book.rating == book_rating:
            book_list.append(book)
    return book_list


@app.get(
    "/books/published-date/q/", response_model=None, status_code=status.HTTP_200_OK
)
async def read_book_by_published_date(
    book_published_date: int = Query(gt=1999, lt=2026)
) -> list[Book | NoReturn]:
    book_list = []
    for book in BOOKS:
        if book.published_date == book_published_date:
            book_list.append(book)
    return book_list


@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    # The .dict() method has been deprecated therefore .model_dump() is being used
    new_book = Book(**book_request.model_dump())
    BOOKS.append(get_book_with_id(new_book))


def get_book_with_id(book: Book) -> Book:
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book


@app.put("/books/update-book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_updated = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_updated = True
    if not book_updated:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found")
