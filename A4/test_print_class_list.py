"""Unit test for print_class_list function."""

# Jacky Zheng
# A01086998
# 03/22/2019

from unittest import TestCase
from unittest.mock import patch, mock_open
from crud import print_class_list
import unittest
import io


class TestPrintClassList(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99"))
    def test_print_class_list(self, mock_stdout):
        expected_output = "Name: Zheng , Jacky | Student Number: A01086998 | Status: True | Grades: [50, 99]\n"
        print_class_list()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.open", mock_open(read_data="Jacky Zheng A01086998 True 50 99\n"
                                                "Chris Thompson A00000000 True 100 100\n"
                                                "No Grades A11111111 False\n"
                                                "Test None A99999999 False"))
    def test_print_class_list_multiple(self, mock_stdout):
        expected_output = "Name: Grades , No | Student Number: A11111111 | Status: False | Grades: []\n" \
                          "Name: None , Test | Student Number: A99999999 | Status: False | Grades: []\n" \
                          "Name: Thompson , Chris | Student Number: A00000000 | Status: True | Grades: [100, 100]\n" \
                          "Name: Zheng , Jacky | Student Number: A01086998 | Status: True | Grades: [50, 99]\n"
        print_class_list()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
