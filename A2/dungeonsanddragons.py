"""Dungeon and Dragons simulator."""

# Jacky Zheng
# A01086998
# 02/07/2019

import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """Roll any sided die any number of times and add the value of the rolls together.

    PARAM: number_of_rolls, a positive integer, how many rolls
    PARAM: number_of_sides, a positive integer, how many sides the die has
    PRECONDITION: number_of_rolls must be a positive integer
    PRECONDITION: number_of_sides must be a positive integer
    RETURN: sum of the rolls as an integer
    >>> random.seed(1)
    >>> (roll_die(3,6))
    8
    """

    roll = random.randint(1, number_of_sides)  # Used recursion for this
    if number_of_rolls == 0:
        return 0  # Base case is 0. If it's 1, then I can roll a 7 with 6 sides
    else:
        return roll + roll_die(number_of_rolls - 1, number_of_sides)  # Subtract 1 roll and keep calling function


def choose_inventory(inventory, selection):
    """Accept a list and integer and randomly select the number of elements from the list.

    PARAM: inventory, a list of at least one string
    PARAM: selection, a positive integer
    PRECONDITION: inventory must be a list with at least one string element
    PRECONDITION: selection must be a positive integer and less than inventory, but greater than 0
    RETURN: a new sorted list of the selected elements
    >>> random.seed(1)
    >>> choose_inventory(['sword', 'bow', 'axe'], 2)
    ['axe', 'sword']
    """
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
        return not_original_list
    else:
        list_2 = sorted(random.sample(inventory, selection))
        return list_2


def generate_name(syllables):
    """Generate a random name with specified number of syllables.

    PARAM: syllables, a positive integer
    PRECONDITION: the function will only work for positive non-zero integers
    RETURN: a random name of requested length as a string
    >>> random.seed(1)
    >>> generate_name(4)
    'Exalatot'
    """
    name = []
    for x in range(0, syllables):
        name.extend(generate_syllable())
    return ''.join(name).title()


def generate_vowel():
    """Generate a random vowel, including 'y'

    RETURN: a random vowel as a string
    >>> random.seed(1)
    >>> generate_vowel()
    ['e']
    """
    return random.sample(['a', 'e', 'i', 'o', 'u', 'y'], 1)


def generate_consonant():
    """Generate a random consonant, including 'y'

    RETURN: a random consonant as a string
    >>> random.seed(1)
    >>> generate_consonant()
    ['g']
    """
    return random.sample(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
                          'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'], 1)


def generate_syllable():
    """Combine a random vowel and consonant to form a syllable

    RETURN: a random syllable as a string
    >>> random.seed(1)
    >>> generate_syllable()
    ['e', 'x']
    """
    return generate_vowel() + generate_consonant()


def create_character(syllables):
    """Create a D&D character with randomly generated name and stats.

    PARAM: syllables, a positive integer
    PRECONDITION: syllables must be a positive integer
    RETURN: dictionary with name, class, HP, XP, and stat rolls
    """
    character = {}
    character.update({'Name': generate_name(syllables)})
    character.update({'Class': classes()})
    character.update({'HP': class_hp(character.get('Class'))})  # Get the value from Class key and pass it to class_hp
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
        return classes()  # If they don't pick a listed class, re-run the function until they do


def class_hp(my_class):
    """Generate HP with appropriate class die.

    PARAM: my_class, a string, an available class
    PRECONDITION: my_class must be a string and an available class
    RETURN: a dice roll as an integer, of the corresponding character dice
    >>> random.seed(1)
    >>> class_hp('barbarian')
    3
    """
    class_dictionary = {'barbarian': roll_die(1, 12), 'bard': roll_die(1, 8), 'cleric': roll_die(1, 8),
                        'druid': roll_die(1, 8), 'fighter': roll_die(1, 10), 'monk': roll_die(1, 8),
                        'paladin': roll_die(1, 10), 'ranger': roll_die(1, 10), 'rogue': roll_die(1, 8),
                        'sorcerer': roll_die(1, 6), 'warlock': roll_die(1, 8), 'wizard': roll_die(1, 6),
                        'blood hunter': roll_die(1, 10)}  # Created a dictionary with the appropriate class die
    if my_class in class_dictionary.keys():  # If my_class is listed, it will return the corresponding class die
        return class_dictionary[my_class]  # Don't need an else statement, as user must pick a listed class to get here


def print_character(character):
    """Accept the character formatted by the create_character function and print it.

    PARAM: character, a well-formed dictionary with character stats
    PRECONDITION: character must be a dictionary generated by the create_character function
    POSTCONDITION: prints the character's information line by line
    """
    for k, v in character.items():
        print(str(k) + ': ' + str(v))  # Prints every key:value pair in character dictionary
    if len(character) == 8:
        print("Inventory:" + str(character[7]))  # If there is an inventory, then print it as well


def combat_round(opponent_one, opponent_two):
    """Simulate combat between two characters with dice rolls and attribute checks.

    PARAM: opponent_one, a well-formed dictionary with character stats
    PARAM: opponent_two, a well-formed dictionary with character stats
    PRECONDITION: will not work unless both parameters are well-formed dictionaries each containing a correct character.
    POSTCONDITION: prints the results of a simulated battle after dice rolls and attribute checks
    """
    opponent_one_strike = roll_die(1, 20)
    print('You rolled', opponent_one_strike)
    opponent_two_strike = roll_die(1, 20)
    print('Enemy rolled', opponent_two_strike)
    if opponent_one_strike == opponent_two_strike:  # If both dice rolls are the same, call function again
        print('Tie! Reroll')
        return combat_round(opponent_one, opponent_two)
    elif opponent_one_strike > opponent_two_strike:  # If your character roll is greater than opponent's
        print('You strike first')
        opponent_one_attack(opponent_one, opponent_two)  # Call opponent_one_attack function
        if opponent_two['HP'] <= 0:  # If enemy dies, then combat ends
            print('Combat ended')
        else:
            opponent_two_attack(opponent_one, opponent_two)  # If they're still alive, call opponent_two_attack function
    elif opponent_two_strike > opponent_one_strike:
        print('Enemy strikes first')
        opponent_two_attack(opponent_one, opponent_two)
        if opponent_one['HP'] <= 0:
            print('Combat ended')
        else:
            opponent_one_attack(opponent_one, opponent_two)


def opponent_one_attack(opponent_one, opponent_two):
    """Simulate combat with opponent_one attacking opponent_two.

    PARAM: opponent_one, a well-formed dictionary with character stats
    PARAM: opponent_two, a well-formed dictionary with character stats
    PRECONDITION: will not work unless both parameters are well-formed dictionaries each containing a correct character.
    POSTCONDITION: prints the results of a simulated battle after dice rolls and attribute checks
    RETURN: opponent_two's HP, only if it is <= 0
    """
    dex_check_roll = roll_die(1, 20)  # Roll a 1d20 to for Dexterity check
    if dex_check_roll > opponent_two['Dexterity']:  # If greater than enemy Dexterity stat, do damage
        damage = class_hp(opponent_one['Class'])  # Roll corresponding class die to determine damage
        print('You rolled a', dex_check_roll, 'and passed the Dexterity check. You did', damage, 'damage')
        opponent_two['HP'] -= damage  # Replace opponent's HP value with the difference
        if opponent_two['HP'] <= 0:  # If the HP is less than or equal to 0, then print death message
            print('Enemy has died')
            return opponent_two['HP']  # Return HP so combat_round function knows whether combat has ended
        else:
            print('Enemy now has', opponent_two['HP'], 'HP')  # If enemy didn't die, then print remaining HP
    else:
        print('You rolled a', dex_check_roll, 'and failed the Dexterity check')  # Prints failed dexterity check roll


def opponent_two_attack(opponent_one, opponent_two):
    """Simulate combat with opponent_two attacking opponent_one.

    PARAM: opponent_one, a well-formed dictionary with character stats
    PARAM: opponent_two, a well-formed dictionary with character stats
    PRECONDITION: will not work unless both parameters are well-formed dictionaries each containing a correct character.
    POSTCONDITION: prints the results of a simulated battle after dice rolls and attribute checks
    RETURN: opponent_one's HP, only if it is <= 0
    """
    dex_check_roll = roll_die(1, 20)
    if dex_check_roll > opponent_one['Dexterity']:
        damage = class_hp(opponent_two['Class'])
        print('Enemy rolled a', dex_check_roll, 'and passed the Dexterity check. They did', damage, 'damage')
        opponent_one['HP'] -= damage
        if opponent_one['HP'] <= 0:
            print('You died')
            return opponent_one['HP']
        else:
            print('You now have', opponent_one['HP'], 'HP')
    else:
        print('Enemy rolled a', dex_check_roll, 'and failed the Dexterity check')


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
    enemy = create_character(4)  # Have user create another character as an opponent
    print_character(enemy)
    combat_round(character, enemy)  # Must have user pick a class to generate another character to fight against


if __name__ == '__main__':
    main()
    doctest.testmod()
