from typing import List, Optional
from sqlalchemy.orm import Session 
from src.models.book import Book
from src.schemas.book_schemas import BookCreate,BookResponse

def add_book(session:Session, book_create:BookCreate)->BookResponse:
    book = Book(**book_create.model_dump())
    session.add(book)
    session.commit()
    session.refresh(book)
    book_response = BookResponse.model_validate(book)
    return book_response

def update_book(session:Session,book_id:int,book_update:BookCreate)->Optional[BookResponse]:
    stmt = session.query(Book).where(Book.id==book_id)
    existing_book = session.scalars(stmt).one_or_none()
    
    if existing_book is None:
       return None
    for key,value in book_update.model_dump().items():
        setattr(existing_book,key,value)
    session.commit()
    session.refresh(existing_book)
    return existing_book

def delete_book(session:Session,book_id:int) -> Optional[BookResponse]:
    stmt = session.query(Book).where(Book.id==book_id)
    existing_book = session.scalars(stmt).one_or_none()
    if existing_book is None:
        return None
    session.delete(existing_book)
    session.commit()
    return BookResponse.model_validate(existing_book)

def get_book(session:Session,book_id:int)-> Optional[BookResponse]:
    stmt = session.query(Book).where(Book.id==book_id) 
    book = session.scalars(stmt).one_or_none()
    if book is None:
        return None
    book_response = BookResponse.model_validate(book) 
    return book_response

def get_books(session:Session) -> List[BookResponse]:
    stmt = session.queryy(Book)
    books = session.scalars(stmt).all()
    return [BookResponse.model_validate(book) for book in books]