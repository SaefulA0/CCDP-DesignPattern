# book_search.py
from search_interface import SearchImplementation


class BookSearch:
    def __init__(self, implementation: SearchImplementation):
        self.implementation = implementation

    def search_books(self, keyword):
        self.implementation.search(keyword)
