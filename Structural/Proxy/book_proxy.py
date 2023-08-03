# book_proxy.py
from book import Book


class BookProxy:
    def __init__(self, title, author):
        self._real_book = Book(title, author)

    def search(self, keyword):
        print("Logging the search request.")
        self._real_book.search(keyword)
