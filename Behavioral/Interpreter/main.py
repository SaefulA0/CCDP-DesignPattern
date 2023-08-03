# main.py
from book_factory import BookFactory


class BookSearchApp:
    def __init__(self):
        self.book_factory = BookFactory()

    def search_book(self, title, author):
        book = self.book_factory.get_book(title, author)
        book.display()


if __name__ == "__main__":
    app = BookSearchApp()
    app.search_book("Book A", "Author X")
    app.search_book("Book B", "Author Y")
    app.search_book("Book A", "Author X")
