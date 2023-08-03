# book.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def accept(self, visitor):
        visitor.visit(self)

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")
