class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                return
        raise Exception("Book not available")


    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                return
        raise Exception("Book not found or already available")
    
    def view_available_books(self):
        return [book for book in self.books if book.available]


