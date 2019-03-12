"""Play a Multi-User Dungeon (MUD)."""

# Jacky Zheng
# A01086998
# 02/26/2019

import random
import doctest
import sud


def cthulu():
    print("You have encountered a Great Old One, Cthulu! ^(;,;)^ It has 15 HP.")
    return {'Name': 'Cthulu', 'HP': 15}


def slime():
    print("You have encountered a cute, but dangerous slime! (´･ω･`) It has 5 HP.")
    return {'Name': 'Slime', 'HP': 5}


def werebear():
    print("You have encountered a fuzzy, but hungry werebear! ʕ•ᴥ•ʔ It has 5 HP.")
    return {'Name': 'Werebear', 'HP': 5}


def table_flipper():
    print("You have encountered a table flipper! Don't get hit by his frustrations! (╯‵□′)╯︵┴─┴ It has 5 HP.")
    return {'Name': 'Table Flipper', 'HP': 5}


def cat():
    print("You have encountered an adorable, but feisty cat! (=ↀωↀ=) It has 5 HP.")
    return {'Name': 'Cat', 'HP': 5}


def monster_picker():
    """Randomly select a monster.

    POSTCONDITION: return a monster

    >>> random.seed(1)
    >>> monster_picker()
    You have encountered a table flipper! Don't get hit by his frustrations! (╯‵□′)╯︵┴─┴ It has 5 HP.
    {'Name': 'Table Flipper', 'HP': 5}
    """
    roll = sud.roll_die(1, 4)
    if roll == 1:
        return slime()
    elif roll == 2:
        return table_flipper()
    elif roll == 3:
        return cat()
    elif roll == 4:
        return werebear()


def main():
    pass


if __name__ == "__main__":
    main()
    doctest.testmod()
