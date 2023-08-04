# main.py
from book import Book
from book_search import BookSearchInterpreter
from book_interpreter import TitleExpression, AuthorExpression


def main():
    books = [
        Book("The Alchemist", "Paulo Coelho", 1988),
        Book("To Kill a Mockingbird", "Harper Lee", 1960),
        Book("1984", "George Orwell", 1949),
        Book("Pride and Prejudice", "Jane Austen", 1813),
        Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    ]

    interpreter = BookSearchInterpreter(books)

    # Interpreting expressions
    title_expr = TitleExpression("the")
    author_expr1 = AuthorExpression("Jane Austen")
    author_expr2 = AuthorExpression("Ernest Hemingway")

    print("Searching for books with title containing 'the':")
    results = interpreter.interpret(title_expr)
    for book in results:
        print(book)

    print("\nSearching for books by 'Jane Austen':")
    results = interpreter.interpret(author_expr1)
    for book in results:
        print(book)

    print("\nSearching for books by 'Ernest Hemingway':")
    results = interpreter.interpret(author_expr2)
    for book in results:
        print(book)


if __name__ == "__main__":
    main()
