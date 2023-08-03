# command.py

class Command:
    def execute(self):
        pass


class SearchBookCommand(Command):
    def __init__(self, book_factory, title, author):
        self.book_factory = book_factory
        self.title = title
        self.author = author

    def execute(self):
        book = self.book_factory.get_book(self.title, self.author)
        book.display()
