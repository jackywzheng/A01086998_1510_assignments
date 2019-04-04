"""Unit test for file_read function."""

# Jacky Zheng
# A01086998
# 03/22/2019

from unittest import TestCase
from unittest.mock import patch, mock_open
from crud import file_read
import unittest.mock
import io


class TestFileRead(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99"))
    def test_file_read(self, mock_stdout):
        file_read()[0].print_info()
        expected_output = "Name: Zheng , Jacky | Student Number: A01086998 | Status: True | Grades: [50, 99]\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_file_read_list(self):
        self.assertIsInstance(file_read(), list)

    def test_file_read_object(self):
        self.assertIsInstance(file_read(), object)
