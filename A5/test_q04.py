from unittest import TestCase
from A5.q04 import selection_sort


class TestSelection_sort(TestCase):
    def test_negative_and_positive_integers(self):
        self.assertEqual(selection_sort([3, 5, 1, 9, -4]), [-4, 1, 3, 5, 9])

    def test_negative_integers(self):
        self.assertEqual(selection_sort([-100, -500, -324, -6, -110]), [-500, -324, -110, -100, -6])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            selection_sort([])

    def test_dictionary(self):
        with self.assertRaises(ValueError):
            selection_sort({"a": 1, "b": 100, "c": 1000, "d": 152})
