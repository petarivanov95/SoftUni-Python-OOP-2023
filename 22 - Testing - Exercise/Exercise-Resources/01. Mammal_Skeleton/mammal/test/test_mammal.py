import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Eddie', 'Dog', 'Woof')

    def test_init(self):
        self.assertEqual(self.mammal.name, 'Eddie')
        self.assertEqual(self.mammal.type, 'Dog')
        self.assertEqual(self.mammal.sound, 'Woof')

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual(result, 'Eddie makes Woof')

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(result, 'animals')

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual(result, 'Eddie is of type Dog')


if __name__ == '__main__':
    unittest.main()
