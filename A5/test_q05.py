from unittest import TestCase
from A5.q05 import cashmoney


class TestCashmoney(TestCase):
    def test_positive_money(self):
        self.assertEqual(cashmoney(66.63),
                         {100: 0, 50: 1, 20: 0, 10: 1, 5: 1, 2: 0, 1: 1, 0.25: 2, 0.1: 1, 0.05: 0, 0.01: 3})

    def test_negative_money(self):
        with self.assertRaises(ValueError):
            cashmoney(-66.63)

    def test_no_money(self):
        self.assertEqual(cashmoney(0.00),
                         {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0})
