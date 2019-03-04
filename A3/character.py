"""Play a Multi-User Dungeon (MUD)."""

# Jacky Zheng
# A01086998
# 02/26/2019


def create_character():
    my_name = input("What is your name?")
    my_name = my_name.strip().lower()
    my_character = {"Name": my_name, "HP": 10, "Class": classes(), "Horizontal": 2, "Vertical": 2}
    print("Your name is", my_name, "\nYour class is", my_character["Class"])
    return my_character


def classes():
    print("Here is a list of classes:\n"
          "Saber - A jack-of-all-trades warrior. "
          "Agile and powerful in close quarters; extremely adept at swordsmanship.\n"
          "Archer - Excellent scouts that excel in strategy and attacking from a distance. "
          "Masters of long ranged warfare.\n"
          "Lancer - Gifted with extreme agility and proficient in hit-and-run tactics "
          "as well as ranged melee weapons such as spears and lances.\n"
          "Berserker - Mad Warrior. Crazed warriors that "
          "have lost almost all traces of their sanity in exchange for great power. (Deal and take 2x damage)")
    my_class = input("What class do you want to play as?")
    my_class = my_class.lower().strip()
    if my_class in "saber,archer,lancer,berserker":
        return my_class.title()
    else:
        print('That is not a class, please select one of the 4 classes')
        return classes()


def hp_recovery(character):
    if character["HP"] < 10:
        character["HP"] += 1
