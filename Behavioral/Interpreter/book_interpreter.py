# book_interpreter.py
from book import Book


class BookExpression:
    def interpret(self, book_list):
        pass


class TitleExpression(BookExpression):
    def __init__(self, keyword):
        self.keyword = keyword

    def interpret(self, book_list):
        return [book for book in book_list if self.keyword.lower() in book.title.lower()]


class AuthorExpression(BookExpression):
    def __init__(self, keyword):
        self.keyword = keyword

    def interpret(self, book_list):
        return [book for book in book_list if self.keyword.lower() in book.author.lower()]
