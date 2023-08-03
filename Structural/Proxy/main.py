# main.py
from book_proxy import BookProxy

if __name__ == "__main__":
    book = BookProxy("Python Programming", "John Doe")

    # Pencarian dilakukan melalui BookProxy
    book.search("Python")
