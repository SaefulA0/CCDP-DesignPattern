from book import Book
from library import Library


class Mediator:
    def __init__(self):
        self.library = Library()

    def add_book(self, title, author):
        book = Book(title, author)
        self.library.add_book(book)

    def show_books(self):
        self.library.show_books()