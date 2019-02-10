"""Unit test for classes function."""

# Jacky Zheng
# A01086998
# 02/09/2019

from unittest import TestCase
from unittest.mock import patch
import dungeonsanddragons


class TestClasses(TestCase):
    # If user inputs an available class, it will return the class
    @patch('dungeonsanddragons.classes', return_value='warrior')
    def test_classes_available_classes(self, mock_classes):
        self.assertEqual(dungeonsanddragons.classes(), 'warrior')

    # If user inputs unavailable class, it will call the function over and over until an available class is inputted
    @patch('dungeonsanddragons.classes', return_value='ninja')
    def test_classes_unavailable_classes(self, mock_classes):
        self.assertEqual(dungeonsanddragons.classes(), dungeonsanddragons.classes())
