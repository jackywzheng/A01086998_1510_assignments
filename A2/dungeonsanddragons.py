"""Dungeon and Dragons simulator."""

# Jacky Zheng
# A01086998
# 02/07/2019

import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """Roll any sided die any number of times and add the value of the rolls together.

    PRECONDITION: number_of_rolls must be a positive integer
    PRECONDITION: number_of_sides must be a positive integer
    RETURN: sum of the rolls as an integer
    """
    roll = random.randint(1, number_of_sides)  # Used recursion for this
    if number_of_rolls == 0:
        return 0  # Base case is 0. If it's 1, then I can roll 7 with 6 sides
    else:
        return roll + roll_die(number_of_rolls - 1, number_of_sides)  # Subtract 1 roll and keep calling


def choose_inventory(inventory, selection):
    """Accept a list and integer and randomly select the number of elements from the list.

    PRECONDITION: inventory must be a list with at least one element
    PRECONDITION: selection must be a positive integer and less than inventory, but greater than 0
    RETURN: a new sorted list of the selected elements"""
    if inventory is [] and selection == 0:
        return []
    elif selection < 0:
        print('You cannot have a negative selection!')
        return None
    elif selection > 0 and selection > len(inventory):
        print('You cannot select more than your inventory size!')
        return None
    elif selection == len(inventory):
        not_original_list = []
        not_original_list.extend(inventory)
        return not_original_list  # Not the original though??
    else:
        list_2 = sorted(random.sample(inventory, selection))
        return list_2


def generate_name(syllables):
    """Generate a random name with specified number of syllables.

    PARAM: syllables, a positive integer
    PRECONDITION: the function will only work for positive non-zero integers
    RETURN: a random name of requested length as a string"""
    name = []
    for x in range(0, syllables):
        name.extend(generate_syllable())
    return ''.join(name).title()


def generate_vowel():
    """Generate a random vowel, including 'y'

    RETURN: a random vowel as a string
    """
    return random.sample(['a', 'e', 'i', 'o', 'u', 'y'], 1)


def generate_consonant():
    """Generate a random consonant, including 'y'

    RETURN: a random consonant as a string
    """
    return random.sample(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                          'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'], 1)


def generate_syllable():
    """Combine a random vowel and consonant to form a syllable

    RETURN: a random syllable as a string
    """
    return generate_vowel() + generate_consonant()


def create_character(syllables):
    """Create a D&D character with randomly generated name and stats.

    PRECONDITION: name_length must be a positive integer
    RETURN: list with name and stat rolls
    """
    character = {}
    character.update({'Name': generate_name(syllables)})
    character.update({'Class': classes()})
    character.update({'HP': class_hp(character.get('Class'))})
    character.update({'Strength': roll_die(3, 6)})
    character.update({'Dexterity': roll_die(3, 6)})
    character.update({'Constitution': roll_die(3, 6)})
    character.update({'Intelligence': roll_die(3, 6)})
    character.update({'Wisdom': roll_die(3, 6)})
    character.update({'Charisma': roll_die(3, 6)})
    character.update({"XP": 0})
    return character


def classes():
    """Pick an available class.

    PRECONDITION: must input one of the listed classes
    RETURN: the selected class
    """
    print("""Here are all the classes:
    barbarian, bard, cleric, druid, fighter, monk, paladin, ranger, rogue, sorcerer, warlock, wizard, blood hunter""")
    my_class = input('What class do you want to play as?')
    my_class = my_class.lower()
    if my_class in "barbarian, bard, cleric, druid, fighter, monk, paladin, " \
                   "ranger, rogue, sorcerer, warlock, wizard, blood hunter":
        return my_class
    else:
        print('That is not a class')
        classes()


def class_hp(my_class):
    """Generate HP with appropriate class die.

    PARAM: my_class, a string, an available class
    PRECONDITION: my_class must be a string and an available class
    RETURN: a dice roll as an integer, of the corresponding character dice"""
    class_dictionary = {'barbarian': roll_die(1, 12), 'bard': roll_die(1, 8), 'cleric': roll_die(1, 8),
                        'druid': roll_die(1, 8), 'fighter': roll_die(1, 10), 'monk': roll_die(1, 8),
                        'paladin': roll_die(1, 10), 'ranger': roll_die(1, 10), 'rogue': roll_die(1, 8),
                        'sorcerer': roll_die(1, 6), 'warlock': roll_die(1, 8), 'wizard': roll_die(1, 6),
                        'blood hunter': roll_die(1, 10)}
    if my_class in class_dictionary.keys():
        return class_dictionary[my_class]


def print_character(character):
    """Accept the character formatted by the create_character function and print it.

    PRECONDITION: character must be a list generated by the create_character function
    POSTCONDITION: prints the character list"""
    for k, v in character.items():
        print(str(k) + ': ' + str(v))
    if len(character) == 8:
        print("Inventory:" + str(character[7]))


def combat_round(opponent_one, opponent_two):
    """Simulate combat with dice rolls and attribute checks.

    PARAM: opponent_one, a well-formed dictionary with character stats
    PARAM: opponent_two, a well-formed dictionary with character stats
    PRECONDITION: will not work unless both parameters are well-formed dictionaries each containing a correct character.
    POSTCONDITION: prints the results of a simulated battle after dice rolls and attribute checks
    """
    opponent_one_strike = roll_die(1, 20)
    opponent_two_strike = roll_die(1, 20)
    if opponent_one_strike == opponent_two_strike:
        combat_round(opponent_one, opponent_two)
    elif opponent_one_strike > opponent_two_strike:
        if opponent_one_strike > opponent_two['Dexterity']:
            opponent_two['HP'] -= class_hp(opponent_one['Class'])
            if opponent_two['HP'] <= 0:
                print('Enemy has died')
            else:
                print('Enemy now has', str(opponent_two['HP']), 'HP')
        else:
            print('Your attack failed')
    elif opponent_two_strike > opponent_one_strike:
        if opponent_two_strike > opponent_one['Dexterity']:
            opponent_one['HP'] -= class_hp(opponent_two['Class'])
            if opponent_one['HP'] <= 0:
                print('You died')
            else:
                print('You now have', str(opponent_one['HP']), 'HP')
        else:
            print('Enemy attack failed')


def main():
    length = int(input('How many syllables do you want your name to have?'))
    character = create_character(length)
    print("Here are some starting items: 'sword', 'bow', 'staff', 'shield', 'potion', 'spear', 'boots'")
    items = int(input('How many items do you want to start out with?'))
    character.update({'Inventory': choose_inventory(['sword', 'bow', 'staff', 'shield', 'potion', 'spear', 'boots']
                                                    , items)})
    print('This is your character\'s stats')
    print_character(character)
    print('Let\'s simulate a fight between your character and another randomly generated character')
    combat_round(character, create_character(5))


if __name__ == '__main__':
    main()
