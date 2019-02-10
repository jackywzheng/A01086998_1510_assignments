"""Unit test for choose_inventory function."""

# Jacky Zheng
# A01086998
# 02/04/2019

from unittest import TestCase
import dungeonsanddragons


class TestChooseInventory(TestCase):
    def test_choose_inventory_selection_and_inventory_equal(self):
        self.assertTrue(type(dungeonsanddragons.choose_inventory(['boots'], 1)) == list)

    def test_choose_inventory_string(self):
        self.assertTrue(type(dungeonsanddragons.choose_inventory(['boots', 'sword', 'staff'], 2)[0]) == str)

    def test_choose_inventory_length(self):
        self.assertTrue(len(dungeonsanddragons.choose_inventory(['boots', 'sword', 'staff'], 2)) == 2)

    def test_choose_inventory_no_inventory(self):
        self.assertTrue(dungeonsanddragons.choose_inventory([], 0) == [])

    def test_choose_inventory_negative(self):
        self.assertEqual(dungeonsanddragons.choose_inventory(
            ['boots', 'sword'], -2), None)

    def test_choose_inventory_larger_than_inventory(self):
        self.assertEqual(dungeonsanddragons.choose_inventory(
            ['boots', 'sword'], 3), None)
