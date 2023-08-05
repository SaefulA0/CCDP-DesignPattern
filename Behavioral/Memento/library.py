from book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        return book

    def show_books(self):
        for book in self.books:
            print(book)