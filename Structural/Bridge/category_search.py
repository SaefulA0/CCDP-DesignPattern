# category_search.py
from search_interface import SearchImplementation


class CategorySearch(SearchImplementation):
    def __init__(self, category_name, book_list):
        self.category_name = category_name
        self.book_list = book_list

    def search(self, keyword):
        print(f"Searching in category: {self.category_name}")
        for book in self.book_list:
            if keyword in book.title or keyword in book.author:
                print(f"Found: {book.title} by {book.author}")
