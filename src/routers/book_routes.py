from typing import List
from src.services import book_service
from src.schemas.book_schemas import BookCreate, BookResponse
from src.database.database import get_session
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

book_router = APIRouter(
    prefix="/api/books",
    tags=["books"]
)

@book_router.get("/", response_model=List[BookResponse])
def get_books(session: Session = Depends(get_session)):
    return book_service.get_books(session)

@book_router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = book_service.get_book(session, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@book_router.post("/", response_model=BookResponse, status_code=201)
def add_book(book: BookCreate, session: Session = Depends(get_session)):
    return book_service.add_book(session, book)

@book_router.put("/{book_id}", response_model=BookResponse)        
def update_book(book_id: int, book: BookCreate, session: Session = Depends(get_session)):
    updated_book = book_service.update_book(session, book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book
    
@book_router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int, session: Session = Depends(get_session)):
    deleted_book = book_service.delete_book(session, book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")