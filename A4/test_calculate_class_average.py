"""Unit test for calculate_class_average function."""

# Jacky Zheng
# A01086998
# 03/22/2019

from unittest import TestCase
from unittest.mock import patch, mock_open
from crud import calculate_class_average


class TestCalculateClassAverage(TestCase):
    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99"))
    def test_calculate_class_average(self):
        self.assertEqual(calculate_class_average(), 74.5)

    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99\n"
                                                "Chris Thompson A00000000 True 100 100 100 100"))
    def test_calculate_class_average_multiple_students(self):
        self.assertEqual(calculate_class_average(), 87.25)

    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99\n"
                                                "Chris Thompson A00000000 100 100 100 100\n"
                                                "No Grades A11111111 False\n"
                                                "Test None A99999999 False"))
    def test_calculate_class_average_multiple_students_some_have_no_grades(self):
        self.assertEqual(calculate_class_average(), 87.25)
