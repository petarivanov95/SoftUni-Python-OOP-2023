class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                user.books.append(book_name)
                self.books_available[author].remove(book_name)
                self.rented_books[user] = {book_name:days_to_return}
                return f"{book_name} successfully rented for the next {days_to_return} days!"
            else:
                return f"The book "{book_name}" is already rented and will be available in {days_to_return provided by the user rented the book} days!"
