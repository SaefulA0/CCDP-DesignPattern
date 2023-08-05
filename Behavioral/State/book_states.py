class BookState:
    def handle_request(self, book):
        pass

    def __str__(self):
        return self.__class__.__name__

class AvailableState(BookState):
    def handle_request(self, book):
        print(f"{book.title} is available for borrowing.")
        book.change_state(BorrowedState())

class BorrowedState(BookState):
    def handle_request(self, book):
        print(f"Sorry, {book.title} is currently borrowed and not available.")

class RepairState(BookState):
    def handle_request(self, book):
        print(f"{book.title} is under repair and not available for borrowing.")