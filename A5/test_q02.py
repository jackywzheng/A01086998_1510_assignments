from unittest import TestCase
from A5.q02 import gcd


class TestGcd(TestCase):
    def test_positive_and_positive(self):
        self.assertEqual(gcd(10, 25), 5)

    def test_negative_and_negative(self):
        with self.assertRaises(ValueError):
            gcd(-100, -50)

    def test_negative_and_zero(self):
        with self.assertRaises(ValueError):
            gcd(-100, 0)

    def test_zero_and_positive(self):
        self.assertEqual(gcd(0, 100), 100)

    def test_prime_numbers(self):
        self.assertEqual(gcd(13, 23), 1)
