import pytest
from library import Library, Book

def test_add_book():
    library = Library()
    book = Book(isbn="1234567890", title="Python 101", author="John Doe", year=2020)
    library.add_book(book)
    assert len(library.books) == 1
    assert library.books[0].title == "Python 101"

def test_borrow_book():
    library = Library()
    book = Book(isbn="1234567890", title="Python 101", author="John Doe", year=2020)
    library.add_book(book)
    library.borrow_book("1234567890")
    assert not library.books[0].available

def test_return_book():
    library = Library()
    book = Book(isbn="1234567890", title="Python 101", author="John Doe", year=2020)
    library.add_book(book)
    library.borrow_book("1234567890")
    library.return_book("1234567890")
    assert library.books[0].available

