# book_search.py

class BookSearchCommand:
    def execute(self):
        pass


class TitleSearch(BookSearchCommand):
    def __init__(self, books, keyword):
        self.books = books
        self.keyword = keyword

    def execute(self):
        print(f"Searching for books with title containing '{self.keyword}':")
        result = [book for book in self.books if self.keyword.lower()
                  in book.title.lower()]
        if result:
            for book in result:
                print(book)
        else:
            print("No books found with the given title.")


class AuthorSearch(BookSearchCommand):
    def __init__(self, books, keyword):
        self.books = books
        self.keyword = keyword

    def execute(self):
        print(f"Searching for books by '{self.keyword}':")
        result = [book for book in self.books if self.keyword.lower()
                  in book.author.lower()]
        if result:
            for book in result:
                print(book)
        else:
            print("No books found by the given author.")
