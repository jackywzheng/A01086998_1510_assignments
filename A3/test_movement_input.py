"""Unit test for movement_input function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import io
import sud
from unittest.mock import patch


class TestMovementInput(TestCase):
    @patch('builtins.input', return_value='n')
    def test_movement_input_north_valid(self, input):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(sud.movement_input(player), [-1, 0])

    @patch('builtins.input', return_value='e')
    def test_movement_input_east_valid(self, input):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(sud.movement_input(player), [0, 1])

    @patch('builtins.input', return_value='w')
    def test_movement_input_west_valid(self, input):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(sud.movement_input(player), [0, -1])

    @patch('builtins.input', return_value='s')
    def test_movement_input_south_valid(self, input):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        self.assertEqual(sud.movement_input(player), [1, 0])

    # Cannot move North as Horizontal = 0, so an error message is printed out.
    @patch('builtins.input', side_effect=['n', 'w'])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_movement_input_invalid(self, mock_stdout, input):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 0, "Vertical": 2}
        expected_output = 'That was not a valid input, or you are trying to move out of the map. ' \
                          'Please enter a valid input.\n'
        sud.movement_input(player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
