from book_states import AvailableState

class Book:
    def __init__(self, title):
        self.title = title
        self.state = AvailableState()

    def change_state(self, state):
        self.state = state

    def request(self):
        self.state.handle_request(self)

    def __str__(self):
        return f"Buku: {self.title}, Status: {self.state}"