"""Unit test for dungeon_map function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import unittest.mock
import io
import sud


class TestDungeonMap(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_dungeon_map_starting_position(self, mock_stdout):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}
        coordinates = [0, 0]
        expected_output = " O O O O O\n" \
                          " O O O O O\n" \
                          " O O X O O\n" \
                          " O O O O O\n" \
                          " O O O O O\n" \
                          "=========================================================" \
                          "==================================================\n"
        sud.dungeon_map(coordinates, player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_dungeon_map_corner_position(self, mock_stdout):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 3, "Vertical": 4}
        coordinates = [1, 0]
        expected_output = " O O O O O\n" \
                          " O O O O O\n" \
                          " O O O O O\n" \
                          " O O O O O\n" \
                          " O O O O X\n" \
                          "=========================================================" \
                          "==================================================\n"
        sud.dungeon_map(coordinates, player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_dungeon_map_middle_middle_position(self, mock_stdout):
        player = {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 4, "Vertical": 3}
        coordinates = [-1, 0]
        expected_output = " O O O O O\n" \
                          " O O O O O\n" \
                          " O O O O O\n" \
                          " O O O X O\n" \
                          " O O O O O\n" \
                          "=========================================================" \
                          "==================================================\n"
        sud.dungeon_map(coordinates, player)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
