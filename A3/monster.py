"""Play a Multi-User Dungeon (MUD)."""

# Jacky Zheng
# A01086998
# 02/26/2019

import random


def cthulu():
    enemy = {'Name': 'Cthulu', 'HP': 15}
    print("You have encountered a Great Old One, Cthulu! ^(;,;)^ It has 15 HP.")
    return enemy


def slime():
    enemy = {'Name': 'Slime', 'HP': 5}
    print("You have encountered a cute, but dangerous slime! (´･ω･`) It has 5 HP.")
    return enemy


def werebear():
    enemy = {'Name': 'Werebear', 'HP': 5}
    print("You have encountered a fuzzy, but hungry werebear! ʕ•ᴥ•ʔ It has 5 HP.")
    return enemy


def table_flipper():
    enemy = {'Name': 'Table Flipper', 'HP': 5}
    print("You have encountered a table flipper! Don't get hit by his frustrations! (╯‵□′)╯︵┴─┴ It has 5 HP.")
    return enemy


def cat():
    enemy = {'Name': 'Cat', 'HP': 5}
    print("You have encountered an adorable, but feisty cat! (=ↀωↀ=) It has 5 HP.")
    return enemy


def monster_picker():
    roll = random.randint(1, 4)
    if roll == 1:
        return slime()
    elif roll == 2:
        return table_flipper()
    elif roll == 3:
        return cat()
    elif roll == 4:
        return werebear()
