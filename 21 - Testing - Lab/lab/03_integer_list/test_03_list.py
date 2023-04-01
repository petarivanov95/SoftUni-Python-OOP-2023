import unittest
from integer_list import IntegerList


class TestIndexList(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_list = IntegerList(1, 2, 3)

    def test_constructor(self):
        self.assertEqual(self.sample_list.int_lst, [1, 2, 3])

    def test_add_func(self):
        self.sample_list.add(5)
        self.assertEqual(self.sample_list.int_lst, [1, 2, 3, 5])

    def test_add_not_int(self):
        with self.assertRaises(ValueError):
            self.sample_list.add('5')

    def test_remove_index(self):
        idx = self.sample_list.remove_index(2)
        self.assertEqual(idx, 3)

    def test_remove_index_out_of_range(self):
        with self.assertRaises(IndexError):
            idx = self.sample_list.remove_index(6)

    def test_get_idx(self):
        num = self.sample_list.get(2)
        self.assertEqual(num, 3)

    def test_get_idx_out_of_range(self):
        with self.assertRaises(IndexError):
            num = self.sample_list.get(6)

    def test_insert_el_not_integer(self):
        with self.assertRaises(ValueError):
            self.sample_list.insert('5', 2)

    def test_insert_idx_out_range(self):
        with self.assertRaises(IndexError):
            self.sample_list.insert(3, 6)

    def test_insert_index(self):
        self.sample_list.insert(12, 2)
        self.assertEqual(self.sample_list.int_lst, [1, 2, 12, 3])

    def test_get_biggest(self):
        self.assertEqual(self.sample_list.get_biggest(), 3)

    def test_get_index(self):
        index = self.sample_list.get_index(3)
        self.assertEqual(index, 2)


if __name__ == '__main__':
    unittest.main()
