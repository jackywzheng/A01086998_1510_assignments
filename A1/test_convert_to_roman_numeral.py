from unittest import TestCase
from A1 import roman_numbers


class TestConvert_to_roman_numeral(TestCase):
    def test_convert_to_roman_numeral_1(self):
        self.assertEqual('I', roman_numbers.convert_to_roman_numeral(1))

    def test_convert_to_roman_numeral_4(self):
        self.assertEqual('IV', roman_numbers.convert_to_roman_numeral(4))

    def test_convert_to_roman_numeral_9(self):
        self.assertEqual('IX', roman_numbers.convert_to_roman_numeral(9))

    def test_convert_to_roman_numeral_10(self):
        self.assertEqual('X', roman_numbers.convert_to_roman_numeral(10))

    def test_convert_to_roman_numeral_49(self):
        self.assertEqual('XLIX', roman_numbers.convert_to_roman_numeral(49))

    def test_convert_to_roman_numeral_50(self):
        self.assertEqual('L', roman_numbers.convert_to_roman_numeral(50))

    def test_convert_to_roman_numeral_99(self):
        self.assertEqual('XCIX', roman_numbers.convert_to_roman_numeral(99))

    def test_convert_to_roman_numeral_100(self):
        self.assertEqual('C', roman_numbers.convert_to_roman_numeral(100))

    def test_convert_to_roman_numeral_499(self):
        self.assertEqual('CDXCIX', roman_numbers.convert_to_roman_numeral(499))

    def test_convert_to_roman_numeral_500(self):
        self.assertEqual('D', roman_numbers.convert_to_roman_numeral(500))

    def test_convert_to_roman_numeral_999(self):
        self.assertEqual('CMXCIX', roman_numbers.convert_to_roman_numeral(999))

    def test_convert_to_roman_numeral_1000(self):
        self.assertEqual('M', roman_numbers.convert_to_roman_numeral(1000))

    def test_convert_to_roman_numeral_10000(self):
        self.assertEqual('MMMMMMMMMM', roman_numbers.convert_to_roman_numeral(10000))
