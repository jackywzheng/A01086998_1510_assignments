from unittest import TestCase
from A5.q01 import sum_of_primes


class TestSum_of_primes(TestCase):
    def test_positive_integers(self):
        self.assertEqual(sum_of_primes(10), 17)

    def test_negative_integers(self):
        with self.assertRaises(ValueError):
            sum_of_primes(-5)

    def test_zero(self):
        self.assertEqual(sum_of_primes(0), 0)
