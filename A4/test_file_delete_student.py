"""Unit test for file_delete_student function."""

# Jacky Zheng
# A01086998
# 03/22/2019

from unittest import TestCase
from unittest.mock import patch, mock_open
from crud import file_delete_student


class TestFileDeleteStudent(TestCase):
    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99"))
    def test_file_delete_student_success(self):
        file_delete_student('A01086998')
        self.assertEqual(file_delete_student('A01086998'), True)

    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99"))
    def test_file_delete_student_fail(self):
        file_delete_student('A00000000')
        self.assertEqual(file_delete_student('A00000000'), False)
