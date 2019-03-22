"""Unit test for save_character function."""

# Jacky Zheng
# A01086998
# 03/10/2019

from unittest import TestCase
import sud
import json


class TestSaveCharacter(TestCase):
    def test_save_character_file_readable(self):  # Make sure that file is readable
        filename = "save.json"
        with open(filename) as file_object:
            my_save = file_object.read()
        self.assertTrue(my_save)

    def test_save_character_same_character_in_file(self):  # Make sure that dictionary in save file matches the mock
        my_save = sud.save_character({"Name": 'Jacky', "HP": 6, "Class": "Berserker", "Horizontal": 3, "Vertical": 0})
        mock_save = {"Name": 'Jacky', "HP": 6, "Class": "Berserker", "Horizontal": 3, "Vertical": 0}
        filename = "save.json"
        with open(filename, 'w') as file_object:
            mock_save = json.dump(mock_save, file_object)
        self.assertEqual(my_save, mock_save)
