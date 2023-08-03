# main.py
from book_factory import BookFactory
from command import SearchBookCommand


class BookSearchApp:
    def __init__(self):
        self.book_factory = BookFactory()

    def search_book(self, title, author):
        search_command = SearchBookCommand(self.book_factory, title, author)
        search_command.execute()


if __name__ == "__main__":
    app = BookSearchApp()
    app.search_book("Book A", "Author X")
    app.search_book("Book B", "Author Y")
    app.search_book("Book A", "Author X")
