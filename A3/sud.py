"""Play a Multi-User Dungeon (MUD)."""

# Jacky Zheng
# A01086998
# 02/26/2019

import random
import monster
import character


def roll_die(number_of_rolls, number_of_sides):
    """Roll any sided die any number of times and add the value of the rolls together.

    PARAM: number_of_rolls, a positive integer, how many rolls
    PARAM: number_of_sides, a positive integer, how many sides the die has
    PRECONDITION: number_of_rolls must be a positive integer
    PRECONDITION: number_of_sides must be a positive integer
    RETURN: sum of the rolls as an integer
    """

    roll = random.randint(1, number_of_sides)  # Used recursion for this
    if number_of_rolls == 0:
        return 0  # Base case is 0. If it's 1, then I can roll a 7 with 6 sides
    else:
        return roll + roll_die(number_of_rolls - 1, number_of_sides)  # Subtract 1 roll and keep calling function


def monster_encounter(player):
    chance = roll_die(1, 10)
    if chance == 5:  # If a 5 is rolled, spawn an enemy encounter. Represents a 10% chance.
        enemy = monster.monster_picker()  # Spawn an enemy from the monster module
        combat_choice(player, enemy)  # Call combat_choice function
    else:
        character.hp_recovery(player)


def boss_encounter(player):
    if player["Horizontal"] == 4 and player["Vertical"] == 4:
        print("You have found the Holy Grail! However, two strong monsters stand between you and the Holy Grail. "
              "Defeat both to claim it and fulfill your wish!")
        combat_choice(player, monster.satan())
        combat_choice(player, monster.cthulu())
        input("You have found the Holy Grail! What is your wish?")


def dungeon_map(horizontal, vertical, player):
    # Takes 3 parameters, horizontal movement, vertical movement, player position in form of dictionary
    dungeon = [['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O']]  # Represents the map
    player["Horizontal"] += horizontal  # Update Horizontal position
    player["Vertical"] += vertical  # Update Vertical position
    dungeon[player["Horizontal"]][player["Vertical"]] = 'X'  # X represents current position
    for row in dungeon:
        for column in row:
            print(column, end=' ')  # Print the map
        print()
    print("===========================================================================================================")
    game_logic(player)


def movement_input(player):
    while True:
        direction = input("Which direction do you want to travel? Type 'n' for North, 'e' for East, "
                          "'w' for West, 's' for South. Type 'quit' to quit playing.")
        direction = direction.lower().strip()
        if direction == 'n' and player["Horizontal"] != 0:  # Can only move North if not at top section
            dungeon_map(-1, 0, player)
        elif direction == 'e' and player["Vertical"] != 4:  # Can only move East if not at right-most section
            dungeon_map(0, 1, player)
        elif direction == 'w' and player["Vertical"] != 0:  # Can only move West if not at left-most section
            dungeon_map(0, -1, player)
        elif direction == 's' and player["Horizontal"] != 4:  # Can only move South if not at bottom section
            dungeon_map(1, 0, player)
        elif direction == 'quit':  # End game if quit
            quit()
        else:
            print("That was not a valid input, or you are trying to move out of the map. Please enter a valid input.")
            movement_input(player)


def combat_choice(player, enemy):
    choice = input("Do you wish to fight the monster? Type 'yes' to fight. Type 'no' to flee.")
    choice.lower().strip()
    if choice == 'yes':  # If player chooses to fight, execute combat_round function
        print("The battle begins!")
        combat_round(player, enemy)
    elif choice == 'no':  # If player chooses to flee, roll a 1d10 to represent a 10% chance
        chance = roll_die(1, 10)
        if chance == 5:  # If it lands on a 5, player takes 1d4 damage
            damage = roll_die(1, 4)
            player["HP"] -= damage
            print('You took', damage, 'damage')
    else:
        print("You did not type a valid input. Type 'yes' or 'no'.")
        combat_choice(player, enemy)  # Call the function again if player typed something else


def combat_round(player, enemy):
    first_attack = roll_die(1, 2)  # Roll a 1d2, represents 50% chance of either character or enemy attacking first
    if first_attack == 1:  # If it's a 1, player attacks first
        print('You attack first')
        while player["HP"] > 0:
            player_attack(player, enemy)
            if enemy['HP'] <= 0:  # If enemy dies, then combat ends
                print('You have slain the monster')
                return
            else:
                enemy_attack(player)  # Enemy attacks if still alive
    else:  # If it's a 2, enemy attacks first
        print('Enemy attacks first')
        while enemy["HP"] > 0:
            enemy_attack(player)
            if player["HP"] <= 0:  # If player dies, then game over
                print('Game over')
                quit()
            else:
                player_attack(player, enemy)  # Player attacks if still alive


def player_attack(player, enemy):
    if player["Class"] == 'Berserker':
        damage = roll_die(1, 12)  # If player is a Berserker, do double damage
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
    if player["Class"] == 'Berserker':
        damage = roll_die(1, 12)  # If player is a Berserker, take double damage
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
    boss_encounter(player)
    monster_encounter(player)
    character.character_status(player)
    movement_input(player)


def main():
    print("You have enlisted into a battle known as the Holy Grail War in order to grant your dearest wish. Navigate "
          "the dungeon, slaughter your enemies, find the Holy Grail, and make your wish come true!")
    my_character = character.create_character()
    print("The X represents your current location. The O's represents available spaces to move into.")
    dungeon_map(0, 0, my_character)


if __name__ == "__main__":
    main()
