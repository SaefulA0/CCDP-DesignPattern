from mediator import Mediator

def main():
    mediator = Mediator()

    # Menambahkan buku ke perpustakaan
    mediator.add_book("Pemrograman Python", "John Doe")
    mediator.add_book("Struktur Data dan Algoritma", "Jane Smith")

    # Menampilkan semua buku
    print("Daftar buku setelah penambahan:")
    mediator.show_books()

if __name__ == "__main__":
    main()