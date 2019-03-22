"""Play a Multi-User Dungeon (MUD)."""

# Jacky Zheng
# A01086998
# 02/26/2019

import random
import monster
import character
import doctest
import json


def roll_die(number_of_rolls, number_of_sides):
    """Roll any sided die any number of times and add the value of the rolls together.

    PARAM: number_of_rolls, a positive integer, how many rolls
    PARAM: number_of_sides, a positive integer, how many sides the die has
    PRECONDITION: number_of_rolls must be a positive integer
    PRECONDITION: number_of_sides must be a positive integer
    RETURN: sum of the rolls as an integer

    >>> random.seed(1)
    >>> (roll_die(3, 6))
    8
    >>> (roll_die(0, 6))
    0
    """

    roll = random.randint(1, number_of_sides)  # Used recursion for this
    if number_of_rolls == 0:
        return 0  # Base case is 0. If it's 1, then I can roll a 7 with 6 sides
    else:
        return roll + roll_die(number_of_rolls - 1, number_of_sides)  # Subtract 1 roll and keep calling function


def monster_encounter():
    """Spawn a monster at a 10% chance.

    RETURN: True if a monster is encountered, otherwise False

    >>> random.seed(1)
    >>> monster_encounter()
    False
    >>> random.seed(13)
    >>> monster_encounter()
    True
    """
    chance = roll_die(1, 10)
    if chance == 5:  # If a 5 is rolled, spawn an enemy encounter. Represents a 10% chance.
        return True
    else:
        return False


def boss_hint(player):
    """Print a helpful hint.

    PARAM: player, a well-formed dictionary with player stats
    PRECONDITION: player must be a well formed dictionary with player stats
    POSTCONDITION: prints a helpful hint.

    >>> boss_hint({"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 1, "Vertical": 3})
    HINT: The boss lies in one of the 4 corners. Once you encounter him, the battle will begin immediately.
    """
    if player["Horizontal"] == 1 and player["Vertical"] == 3:
        print("HINT: The boss lies in one of the 4 corners. Once you encounter him, the battle will begin immediately.")
    elif player["Horizontal"] == 3 and player["Vertical"] == 1:
        print("HINT: The boss lies in one of the 4 corners. Once you encounter him, the battle will begin immediately")


def boss_encounter(player):
    """Fight a boss monster and complete the game.

    PARAM: player, a well-formed dictionary with player stats
    PRECONDITION: player must be a well formed dictionary with player stats
    POSTCONDITION: prints winning messages if boss is defeated
    """
    if player["Horizontal"] == 4 and player["Vertical"] == 4:
        print("You have found the Holy Grail! However, a strong monster stands between you and the Holy Grail. "
              "Defeat the monster to claim the Holy Grail and fulfill your wish!")
        win = combat_round(player, monster.cthulu())
        if win is True:
            input("You have found the Holy Grail! What is your wish?")
            print("You take a drink from the Holy Grail in order for it to grant your wish, only to discover that\n"
                  "it's just watermelon juice. You feel cheated, but at least your thirst was quenched."
                  "Thanks for playing!")
            return True
        else:
            quit()


def dungeon_map(coordinates, player):
    """Print a map with available movement positions as O's and display current location as an X.

    PARAM: coordinates, a list of two integers between -1 and 1 inclusive
    PARAM: player, a well-formed dictionary with player stats
    PRECONDITION: coordinates must be a list of two integers between -1 and 1 inclusive
    PRECONDITION: player must be a well-formed dictionary with player stats
    POSTCONDITION: prints a map that displays current player location

    >>> dungeon_map([0, 0], {"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2})
     O O O O O
     O O O O O
     O O X O O
     O O O O O
     O O O O O
    ===========================================================================================================

    """
    dungeon = [['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O']]  # Represents the map
    player["Horizontal"] += coordinates[0]  # Update Horizontal position
    player["Vertical"] += coordinates[1]  # Update Vertical position
    dungeon[player["Horizontal"]][player["Vertical"]] = 'X'  # X represents current position
    for row in dungeon:
        for column in row:
            print('', column, end='')  # Print the map, must have blank space before or doctest will always fail
        print()
    print("===========================================================================================================")


def movement_input(player):
    """Input a direction and move in that direction if possible.

    PARAM: player, a well-formed dictionary with player stats
    PRECONDITION: player must be a well-formed dictionary with player stats
    RETURN: corresponding list of two integers indicating movement
    """
    direction = input("Which direction do you want to travel? Type 'n' for North, 'e' for East, "
                      "'w' for West, 's' for South. Type 'quit' to save and quit playing.")
    direction = direction.lower().strip()
    if direction == 'n' and player["Horizontal"] != 0:  # Can only move North if not at top section
        return [-1, 0]
    elif direction == 'e' and player["Vertical"] != 4:  # Can only move East if not at right-most section
        return [0, 1]
    elif direction == 'w' and player["Vertical"] != 0:  # Can only move West if not at left-most section
        return [0, -1]
    elif direction == 's' and player["Horizontal"] != 4:  # Can only move South if not at bottom section
        return [1, 0]
    elif direction == 'quit':  # Save the character in a JSON file and quit the game
        save_character(player)
        quit()
    else:
        print("That was not a valid input, or you are trying to move out of the map. Please enter a valid input.")
        return movement_input(player)  # Call function again if invalid input


def combat_choice(player, enemy):
    """Fight or flee from an enemy encounter.

    PARAM: player, a well-formed dictionary with character stats
    PARAM: enemy, a well-formed dictionary with enemy stats
    PRECONDITION: will not work unless both parameters are well-formed dictionaries each containing HP stats
    POSTCONDITION: prints the results of a simulated battle after dice rolls
    """
    choice = input("Do you wish to fight the monster? Type 'yes' to fight. Type 'no' to flee.")
    choice.lower().strip()
    if choice == 'yes':  # If player chooses to fight, execute combat_round function
        print("The battle begins!")
        if combat_round(player, enemy) is False:
            return False
    elif choice == 'no':  # If player chooses to flee, roll a 1d10 to represent a 10% chance
        print("You have fled!")
        chance = roll_die(1, 10)
        if chance == 5:  # If it lands on a 5, player takes 1d4 damage
            damage = roll_die(1, 4)
            player["HP"] -= damage
            print('You took', damage, 'damage while your back was turned!')
    else:
        print("You did not type a valid input. Type 'yes' or 'no'.")
        return combat_choice(player, enemy)  # Call the function again if player typed something else


def combat_round(player, enemy):
    """Simulate combat between the player and an enemy with dice rolls until one of them dies.

    PARAM: player, a well-formed dictionary with character stats
    PARAM: enemy, a well-formed dictionary with enemy stats
    PRECONDITION: will not work unless both parameters are well-formed dictionaries each containing HP stats
    POSTCONDITION: prints the results of a simulated battle after dice rolls

    >>> random.seed(1)
    >>> combat_round({"Name": 'Jacky', "HP": 10, "Class": "Berserker", "Horizontal": 2, "Vertical": 2}, \
    {'Name': 'Slime', 'HP': 5})
    You attack first
    ===========================================================================================================
    You did 6 damage
    Enemy has died
    You have slain the monster
    True

    >>> random.seed(2)
    >>> combat_round({"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}, \
    {'Name': 'Slime', 'HP': 5})
    You attack first
    ===========================================================================================================
    You did 1 damage
    Enemy now has 4 HP
    ===========================================================================================================
    Enemy did 2 damage
    You now have 8 HP
    ===========================================================================================================
    You did 6 damage
    Enemy has died
    You have slain the monster
    True
    """
    first_attack = roll_die(1, 2)  # Roll a 1d2, represents 50% chance of either character or enemy attacking first
    if first_attack == 1:  # If it's a 1, player attacks first
        print('You attack first')
        while player["HP"] > 0:
            if player_attack(player, enemy) <= 0:  # If enemy dies, then combat ends
                print('You have slain the monster')
                return True
            else:
                if enemy_attack(player) <= 0:  # Enemy attacks if still alive
                    return False
    else:  # If it's a 2, enemy attacks first
        print('Enemy attacks first')
        while enemy["HP"] > 0:
            if enemy_attack(player) <= 0:  # If player dies, then game over
                print('Game over')
                return False
            else:
                player_attack(player, enemy)  # Player attacks if still alive


def player_attack(player, enemy):
    """Simulate a combat round when player attacks the enemy.

    PARAM: player, a well-formed dictionary with character stats
    PARAM: enemy, a well-formed dictionary with enemy stats
    PRECONDITION: will not work unless both parameters are well-formed dictionaries each containing HP stats
    POSTCONDITION: prints the results of the battle after dice rolls

    >>> random.seed(1)
    >>> player_attack({"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2}, \
    {'Name': 'Slime', 'HP': 5})
    ===========================================================================================================
    You did 2 damage
    Enemy now has 3 HP
    3
    """
    if player["Class"] == 'Berserker':
        damage = roll_die(1, 6) * 2  # If player is a Berserker, do double damage
    else:
        damage = roll_die(1, 6)  # If player is any other class, do regular damage
    print("===========================================================================================================")
    print('You did', damage, 'damage')
    enemy['HP'] -= damage  # Replace enemy's HP value with the difference
    if enemy['HP'] <= 0:  # If the HP is less than or equal to 0, then print death message
        print('Enemy has died')
        return enemy['HP']  # Return HP so combat_round function knows whether combat has ended
    else:
        print('Enemy now has', enemy['HP'], 'HP')  # If enemy didn't die, then print remaining HP
        return enemy['HP']


def enemy_attack(player):
    """Simulate a combat round when player gets attacked.

    PARAM: player, a well-formed dictionary with character stats
    PRECONDITION: player must be a well-formed dictionary with HP stat
    POSTCONDITION: prints the results of the battle after dice rolls

    >>> random.seed(1)
    >>> enemy_attack({"Name": 'Jacky', "HP": 10, "Class": "Saber", "Horizontal": 2, "Vertical": 2})
    ===========================================================================================================
    Enemy did 2 damage
    You now have 8 HP
    8
    """
    if player["Class"] == 'Berserker':
        damage = roll_die(1, 6) * 2  # If player is a Berserker, take double damage
    else:
        damage = roll_die(1, 6)  # If player is any other class, take regular damage
    print("===========================================================================================================")
    print('Enemy did', damage, 'damage')
    player['HP'] -= damage  # Replace character's HP value with the difference
    if player['HP'] <= 0:  # If the HP is less than or equal to 0, then print death message
        print('You died')
        return player['HP']  # Return HP so combat_round function knows whether combat has ended
    else:
        print('You now have', player['HP'], 'HP')  # If you didn't die, then print remaining HP
        return player['HP']


def game_logic(player):
    """Execute the game logic.

    PARAM: player, a well-formed dictionary with character stats
    PRECONDITION: player must be a well-formed dictionary with HP stat
    POSTCONDITION: game is executed
    """
    while True:
        win = boss_encounter(player)
        if win is True:
            break
        encounter = monster_encounter()
        if encounter is False:
            character.hp_recovery(player)
        else:
            if combat_choice(player, monster.monster_picker()) is False:
                break
        character.character_status(player)
        boss_hint(player)
        dungeon_map(movement_input(player), player)


def save_character(player):
    """Save character state.

    PARAM: player, a well formed dictionary with character stats
    POSTCONDITION: player must be a well formed dictionary with character stats
    POSTCONDITION: saves character dictionary in a .json file
    """
    filename = 'save.json'
    with open(filename, 'w') as file_object:
        json.dump(player, file_object)


def main():
    """Drives the function.
    """
    print("You have enlisted into a battle known as the Holy Grail War in order to grant your dearest wish.\nNavigate "
          "the dungeon, slaughter your enemies, find the Holy Grail, and make your wish come true!")
    player = character.create_character()
    print("The X represents your current location. The O's represents available spaces to move into.")
    dungeon_map([0, 0], player)
    game_logic(player)


if __name__ == "__main__":
    main()
    doctest.testmod()
