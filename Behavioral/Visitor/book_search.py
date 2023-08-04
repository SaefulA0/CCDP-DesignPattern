# book_search.py
from book import Book


class BookSearchVisitor:
    def visit_title(self, book_list, keyword):
        pass

    def visit_author(self, book_list, keyword):
        pass


class BookSearchByTitle(BookSearchVisitor):
    def visit_title(self, book_list, keyword):
        print(f"Searching for books with title containing '{keyword}':")
        result = [book for book in book_list if keyword.lower()
                  in book.title.lower()]
        if result:
            for book in result:
                print(book)
        else:
            print("No books found with the given title.")


class BookSearchByAuthor(BookSearchVisitor):
    def visit_author(self, book_list, keyword):
        print(f"Searching for books by '{keyword}':")
        result = [book for book in book_list if keyword.lower()
                  in book.author.lower()]
        if result:
            for book in result:
                print(book)
        else:
            print("No books found by the given author.")
