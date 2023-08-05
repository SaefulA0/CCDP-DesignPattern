from book_memento import book_memento


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Buku: {self.title} - Penulis: {self.author}"

    def create_memento(self):
        return book_memento(self.title, self.author)

    def restore_memento(self, memento):
        self.title = memento.title
        self.author = memento.author