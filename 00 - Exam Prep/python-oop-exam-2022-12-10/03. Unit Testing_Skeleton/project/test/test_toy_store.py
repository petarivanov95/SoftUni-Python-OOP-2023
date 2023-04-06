from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_add_toy_successful(self):
        result = self.store.add_toy("A", "Teddy Bear")
        self.assertEqual(result, "Toy:Teddy Bear placed successfully!")
        self.assertEqual(self.store.toy_shelf["A"], "Teddy Bear")

    def test_add_toy_shelf_not_exist(self):
        with self.assertRaises(Exception):
            self.store.add_toy("H", "Car")

    def test_add_toy_already_in_shelf(self):
        self.store.add_toy("B", "Doll")
        with self.assertRaises(Exception):
            self.store.add_toy("B", "Doll")

    def test_add_toy_shelf_already_taken(self):
        self.store.add_toy("C", "Action Figure")
        with self.assertRaises(Exception):
            self.store.add_toy("C", "Board Game")

    def test_remove_toy_successful(self):
        self.store.add_toy("D", "Puzzle")
        result = self.store.remove_toy("D", "Puzzle")
        self.assertEqual(result, "Remove toy:Puzzle successfully!")
        self.assertIsNone(self.store.toy_shelf["D"])

    def test_remove_toy_shelf_not_exist(self):
        with self.assertRaises(Exception):
            self.store.remove_toy("H", "Car")

    def test_remove_toy_not_in_shelf(self):
        self.store.add_toy("E", "LEGO")
        with self.assertRaises(Exception):
            self.store.remove_toy("E", "Puzzle")
