from unittest import TestCase
from A5 import q09


class TestConvert_to_base_ten(TestCase):
    def test_convert_to_base_ten(self):
        self.assertEqual(q09.convert_to_base_ten(4323, 5), 588)

    def test_convert_to_other_base(self):
        self.assertEqual(q09.convert_to_other_base(588, 2), "1001001100")

    def test_base_conversion(self):
        self.assertEqual(q09.base_conversion(5, 4323, 2), 1001001100)
