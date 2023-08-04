# main.py
from book import Book
from book_search import TitleSearch, AuthorSearch
from command_invoker import CommandInvoker


def main():
    books = [
        Book("The Alchemist", "Paulo Coelho", 1988),
        Book("To Kill a Mockingbird", "Harper Lee", 1960),
        Book("1984", "George Orwell", 1949),
        Book("Pride and Prejudice", "Jane Austen", 1813),
        Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    ]

    invoker = CommandInvoker()
    invoker.add_command(TitleSearch(books, "the"))
    invoker.add_command(AuthorSearch(books, "Jane Austen"))
    invoker.add_command(AuthorSearch(books, "Ernest Hemingway"))

    invoker.run_commands()


if __name__ == "__main__":
    main()
