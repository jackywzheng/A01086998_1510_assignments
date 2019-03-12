"""Unit test for create_character function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import io
import character
from unittest.mock import patch


class TestCreateCharacter(TestCase):
    @patch('builtins.input', return_value='Jacky')
    @patch('character.classes', return_value='Archer')
    def test_create_character(self, mock_classes, input):
        self.assertEqual(character.create_character(), {"Name": 'Jacky', "HP": 10, "Class": 'Archer'
                         , "Horizontal": 2, "Vertical": 2})

    @patch('builtins.input', return_value='Jacky')
    @patch('character.classes', return_value='Archer')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_message(self, mock_stdout, mock_classes, input):
        expected_output = "Your name is Jacky \nYour class is Archer\n"
        character.create_character()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
