# book_category.py
from component import BookComponent


class BookCategory(BookComponent):
    def __init__(self, category_name):
        self.category_name = category_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search(self, keyword):
        print(f"Searching in category: {self.category_name}")
        for book in self.books:
            book.search(keyword)
