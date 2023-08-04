# book_search.py
from book_interpreter import BookExpression, TitleExpression, AuthorExpression


class BookSearchInterpreter:
    def __init__(self, book_list):
        self.book_list = book_list

    def interpret(self, expression):
        return expression.interpret(self.book_list)
