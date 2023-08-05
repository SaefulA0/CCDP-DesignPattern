from library import Library
from memento_caretaker import MementoCaretaker

def main():
    library = Library()
    caretaker = MementoCaretaker()

    # Menambahkan buku ke perpustakaan
    book1 = library.add_book("Pemrograman Python", "John Doe")
    book2 = library.add_book("Struktur Data dan Algoritma", "Jane Smith")

    # Menyimpan status buku pertama
    caretaker.add_memento(book1.create_memento())

    # Menambahkan buku baru ke perpustakaan
    book3 = library.add_book("Pola Desain", "Michael Johnson")

    # Menampilkan semua buku
    print("Daftar buku setelah penambahan:")
    library.show_books()

    # Mengembalikan status buku pertama
    print("\nMengembalikan status buku pertama:")
    book1.restore_memento(caretaker.get_memento(0))

    # Menampilkan semua buku setelah pengembalian status
    print("\nDaftar buku setelah pengembalian status:")
    library.show_books()

if __name__ == "__main__":
    main()