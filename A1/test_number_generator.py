from unittest import TestCase
import lotto


class TestNumberGenerator(TestCase):
    def test_number_generator_sorted_and_unique(self):
        lottery = lotto.number_generator()
        self.assertTrue(lottery[0] < lottery[1] < lottery[2] < lottery[3] < lottery[4] < lottery[5])

    def test_number_generator_6_numbers(self):
        self.assertTrue(len(lotto.number_generator()) == 6, lotto.number_generator())

    def test_number_generator_integer(self):
        self.assertEqual(int, type(sum(lotto.number_generator())))

    def test_number_generator_between_1_to_49(self):
        lottery = lotto.number_generator()
        self.assertTrue(lottery[0] > 0 and lottery[5] < 50)





