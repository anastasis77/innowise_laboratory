from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from database import SessionLocal, engine
from models import Base, Book

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def create_book(title: str, author: str, year: Optional[int] = None, db: Session = Depends(get_db)):
    new_book = Book(title=title, author=author, year=year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"id": new_book.id, "title": new_book.title, "author": new_book.author, "year": new_book.year}

@app.get("/books/")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return [{"id": book.id, "title": book.title, "author": book.author, "year": book.year} for book in books]

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted"}

@app.put("/books/{book_id}")
def update_book(book_id: int, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if title:
        book.title = title
    if author:
        book.author = author
    if year:
        book.year = year
    db.commit()
    db.refresh(book)
    return {"id": book.id, "title": book.title, "author": book.author, "year": book.year}

@app.get("/books/search/")
def search_books(title: Optional[str] = Query(None), author: Optional[str] = Query(None), year: Optional[int] = Query(None), db: Session = Depends(get_db)):
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(Book.year == year)
    books = query.all()
    return [{"id": book.id, "title": book.title, "author": book.author, "year": book.year} for book in books]