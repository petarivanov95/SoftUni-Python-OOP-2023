import unittest


class Book:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)


# class TestBook(unittest.TestCase):
#     def setUp(self) -> None:
#         self.book = Book("My Book", "Me", 200)
#
#     def test_name_of_book(self):
#         result = self.book.name
#         self.assertEqual(result, 'My Book1')
#
#
# if __name__ == '__main__':
#     unittest.main()
