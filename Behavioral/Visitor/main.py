# main.py
from book import Book
from book_manager import BookManager
from book_search import BookSearchByTitle, BookSearchByAuthor


def main():
    book_manager = BookManager()

    book_manager.add_book(Book("The Alchemist", "Paulo Coelho", 1988))
    book_manager.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    book_manager.add_book(Book("1984", "George Orwell", 1949))
    book_manager.add_book(Book("Pride and Prejudice", "Jane Austen", 1813))
    book_manager.add_book(
        Book("The Catcher in the Rye", "J.D. Salinger", 1951))

    search_visitor = BookSearchByTitle()
    book_manager.accept(search_visitor, "the")

    search_visitor = BookSearchByAuthor()
    book_manager.accept(search_visitor, "Jane Austen")

    search_visitor = BookSearchByAuthor()
    book_manager.accept(search_visitor, "Ernest Hemingway")


if __name__ == "__main__":
    main()
