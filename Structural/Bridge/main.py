# main.py
from book_search import BookSearch
from title_author_search import TitleAuthorSearch
from category_search import CategorySearch


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


if __name__ == "__main__":
    book_list = [
        Book("Python Programming", "John Doe"),
        Book("Data Science Basics", "Jane Smith"),
        Book("Introduction to Algorithms", "Alice Johnson"),
    ]

    title_author_search = TitleAuthorSearch(book_list)
    category_search = CategorySearch("Programming", book_list)

    book_search = BookSearch(title_author_search)
    book_search.search_books("Python")

    print("===========")

    book_search.implementation = category_search
    book_search.search_books("Introduction")
