from project.library import Library
from project.user import User
from project.registration import Registration
from typing import List, Dict



class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}  # { author: [book1, book2...] }
        self.rented_books: Dict[str: Dict[str: int]] = {}  # { username: { book_name: days_to_return } }

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for data in self.rented_books.values():
            if book_name in data:
                return f'The book "{book_name}" is already rented and will be available in {data[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> [str, None]:
        if book_name in self.rented_books[user.username]:
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"



user = User(12, 'Peter')
library = Library()
registration = Registration()
registration.add_user(user, library)
library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})
library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user)
print(user)
