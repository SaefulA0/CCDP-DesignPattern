# main.py
from book_factory import BookFactory
from visitor import BookSearchVisitor


class BookSearchApp:
    def __init__(self):
        self.book_factory = BookFactory()

    def search_book(self, title, author):
        visitor = BookSearchVisitor(title, author)
        for book in self.book_factory._books.values():
            book.accept(visitor)

        found_books = visitor.get_found_books()
        if found_books:
            print(
                f"Found {len(found_books)} book(s) with title '{title}' and author '{author}':")
            for book in found_books:
                book.display()
        else:
            print(f"No book found with title '{title}' and author '{author}'.")


if __name__ == "__main__":
    app = BookSearchApp()
    app.search_book("Book A", "Author X")
    app.search_book("Book B", "Author Y")
    app.search_book("Book A", "Author X")
