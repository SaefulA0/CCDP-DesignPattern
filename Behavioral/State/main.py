from library import Library
from book_states import RepairState, BorrowedState

def main():
    library = Library()

    book1 = library.add_book("Pemrograman Python")
    book2 = library.add_book("Struktur Data dan Algoritma")

    print("Status awal buku:")
    library.show_books()

    # Mengubah status buku menjadi 'BorrowedState'
    book1.change_state(BorrowedState())

    # Mencoba menambahkan buku baru ketika ada buku dalam status 'BorrowedState'
    try:
        book3 = library.add_book("Pola Desain")
    except Exception as e:
        print(f"Error: {e}")

    # Mengubah status buku menjadi 'RepairState'
    book2.change_state(RepairState())

    print("\nStatus buku setelah perubahan status:")
    library.show_books()

if __name__ == "__main__":
    main()