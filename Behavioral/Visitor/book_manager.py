# book_manager.py
from book import Book


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def accept(self, visitor, keyword):
        visitor.visit_title(self.books, keyword)
        visitor.visit_author(self.books, keyword)
