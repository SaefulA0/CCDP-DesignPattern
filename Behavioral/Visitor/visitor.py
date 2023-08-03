# visitor.py

class BookSearchVisitor:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.found_books = []

    def visit(self, book):
        if book.title == self.title and book.author == self.author:
            self.found_books.append(book)

    def get_found_books(self):
        return self.found_books
