# title_author_search.py
from search_interface import SearchImplementation


class TitleAuthorSearch(SearchImplementation):
    def __init__(self, book_list):
        self.book_list = book_list

    def search(self, keyword):
        for book in self.book_list:
            if keyword in book.title or keyword in book.author:
                print(f"Found: {book.title} by {book.author}")
