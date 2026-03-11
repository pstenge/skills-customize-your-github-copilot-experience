from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory data store for the assignment.
books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
    {"id": 2, "title": "Refactoring", "author": "Martin Fowler", "year": 1999},
]


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Books API"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: BookCreate):
    next_id = max((item["id"] for item in books), default=0) + 1
    new_book = {
        "id": next_id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
    }
    books.append(new_book)
    return new_book
