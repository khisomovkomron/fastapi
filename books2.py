from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of book",
                                       max_length=100,
                                       min_length=1)
    rating: int = Field(gt=-1, lt=101)
    
    class Config:
        schema_extra = {
            "example": {
                "id": "c2df52dc-7375-4ce7-bc31-b5ec14c8b333",
                'title': "Computer science pro",
                'author': 'Codingwithroby',
                'description': 'A very nice description of a book',
                'rating': 75
            }
        }


BOOKS = []


@app.get('/')
async def read_all_books(books_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()
        
    if books_to_return and len(BOOKS) >= books_to_return > 0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books
        
    return BOOKS


@app.get('/book/{book_id}')
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return book


@app.put('/{book_id}')
async def update_book(book_id: UUID, book: Book):
    counter = 0
    
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]


@app.delete('/{book_id}')
async def delete_book(book_id: UUID):
    counter = 0
    
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID: {book_id} deleted'
    


def create_books_no_api():
    book_1 = Book(id="6f0d7202-b8fa-4410-8064-1b09cfe7b1d4",
                  title="TItle 1",
                  author='Author 1',
                  description='Description 1',
                  rating=60)
    book_2 = Book(id="469b6229-d2e9-499f-b8b2-99d0680dbd56",
                  title="TItle 2",
                  author='Author 2',
                  description='Description 2',
                  rating=70)
    book_3 = Book(id="fea83082-0593-48b9-8c22-a501e6128d50",
                  title="TItle 3",
                  author='Author 3',
                  description='Description 3',
                  rating=80)
    book_4 = Book(id="c2df52dc-7375-4ce7-bc31-b5ec14c8b330",
                  title="TItle 4",
                  author='Author 4',
                  description='Description 4',
                  rating=90)
    
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
