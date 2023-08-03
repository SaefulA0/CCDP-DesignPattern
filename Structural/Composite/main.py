# main.py
from book import Book
from book_category import BookCategory

if __name__ == "__main__":
    # Membuat beberapa buku individu
    book1 = Book("Python Programming", "John Doe")
    book2 = Book("Data Science Basics", "Jane Smith")
    book3 = Book("Introduction to Algorithms", "Alice Johnson")

    # Membuat kategori buku dan menambahkan beberapa buku ke dalamnya
    programming_books = BookCategory("Programming")
    programming_books.add_book(book1)
    programming_books.add_book(book2)

    algorithms_books = BookCategory("Algorithms")
    algorithms_books.add_book(book3)

    # Menambahkan subkategori di bawah kategori Algorithms
    algorithms_subcategory = BookCategory("Data Structures")
    algorithms_subcategory.add_book(
        Book("Data Structures in Python", "Bob Brown"))
    algorithms_subcategory.add_book(
        Book("Data Structures in Java", "Charlie Green"))

    algorithms_books.add_book(algorithms_subcategory)

    # Melakukan pencarian di level kategori dan buku individu
    print("=== Search Results ===")
    keyword = "Python"
    programming_books.search(keyword)
    algorithms_books.search(keyword)
