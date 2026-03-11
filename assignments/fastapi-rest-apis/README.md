# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a beginner-friendly REST API using FastAPI by defining routes, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI app and implement basic REST endpoints for managing a small in-memory list of books.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Implement `GET /` that returns a welcome JSON message.
- Implement `GET /books` that returns all books.
- Implement `GET /books/{book_id}` that returns one book by id.
- Return a clear error message if a requested book id does not exist.


### 🛠️ Add Input Validation and Create Endpoint

#### Description
Use a Pydantic model to validate incoming data and create a `POST` endpoint to add a new book.

#### Requirements
Completed program should:

- Define a `BookCreate` model with `title`, `author`, and `year` fields.
- Implement `POST /books` that accepts valid JSON and adds a new book.
- Auto-generate a numeric id for each new book.
- Return the created book as JSON.
- Example request body:
  ```json
  {
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "year": 2008
  }
  ```
