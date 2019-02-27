"""Play a Multi-User Dungeon (MUD)."""

# Jacky Zheng
# A01086998
# 02/26/2019


def character():
    name = input("What is your name?")
    my_character = {"Name": name, "HP": 10}
    return my_character