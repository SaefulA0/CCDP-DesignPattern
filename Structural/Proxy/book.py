# book.py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def search(self, keyword):
        if keyword in self.title or keyword in self.author:
            print(f"Found: {self.title} by {self.author}")
