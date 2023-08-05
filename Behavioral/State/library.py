from book import Book
from book_states import AvailableState

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        book = Book(title)
        self.books.append(book)
        return book

    def search_book(self, title):
        found_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        return found_books

    def show_books(self):
        for book in self.books:
            print(book)