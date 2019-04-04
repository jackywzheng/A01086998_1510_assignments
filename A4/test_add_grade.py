"""Unit test for add_grade function."""

# Jacky Zheng
# A01086998
# 03/22/2019

from unittest import TestCase
from unittest.mock import patch, mock_open
from crud import add_grade


class TestAddGrade(TestCase):
    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99"))
    @patch('builtins.input', return_value='A00000000')
    def test_add_grade_student_number_not_found(self, input):
        self.assertEqual(add_grade(), False)

    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99"))
    @patch('builtins.input', return_value='A01086998')
    def test_add_grade_student_number_found(self, input):
        self.assertEqual(add_grade(), True)
