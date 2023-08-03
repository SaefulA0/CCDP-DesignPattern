# book_factory.py
from book import Book


class BookFactory:
    _books = {}

    def get_book(self, title, author):
        key = f"{title}_{author}"
        if key not in self._books:
            self._books[key] = Book(title, author)
        return self._books[key]
