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
        enemy = monster.monster()  # Spawn an enemy from the monster module
        combat_choice(player, enemy)  # Call combat_choice function


def dungeon_map(horizontal, vertical, player):
    # Takes 3 parameters, horizontal movement, vertical movement, player position in form of dictionary
    dungeon = [['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O']]
    player["Horizontal"] += horizontal
    player["Vertical"] += vertical
    dungeon[player["Horizontal"]][player["Vertical"]] = 'X'
    for row in dungeon:
        for column in row:
            print(column, end=' ')  # Print
        print()
    character.hp_recovery(player)
    monster_encounter(player)
    movement_input(player)


def movement_input(player):
    while True:
        direction = input("Which direction do you want to travel? Type 'n' for North, 'e' for East, "
                          "'w' for West, 's' for South. Type 'quit' to quit playing.")
        direction = direction.lower().strip()
        if direction == 'n':
            dungeon_map(-1, 0, player)
        elif direction == 'e':
            dungeon_map(0, 1, player)
        elif direction == 'w':
            dungeon_map(0, -1, player)
        elif direction == 's':
            dungeon_map(1, 0, player)
        elif direction == 'quit':
            break
        else:
            print("That was not a valid input. Please enter a valid input.")
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
            player_attack(enemy)
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
                return
            else:
                player_attack(enemy)  # Player attacks if still alive


def player_attack(enemy):
    damage = roll_die(1, 6)  # Roll corresponding 1d6 to determine damage
    print('You did', damage, 'damage')
    enemy['HP'] -= damage  # Replace enemy's HP value with the difference
    if enemy['HP'] <= 0:  # If the HP is less than or equal to 0, then print death message
        print('Enemy has died')
        return enemy['HP']  # Return HP so combat_round function knows whether combat has ended
    else:
        print('Enemy now has', enemy['HP'], 'HP')  # If enemy didn't die, then print remaining HP
        return enemy['HP']


def enemy_attack(player):
    damage = roll_die(1, 6)  # Roll corresponding 1d6 to determine damage
    print('Enemy did', damage, 'damage')
    player['HP'] -= damage  # Replace character's HP value with the difference
    if player['HP'] <= 0:  # If the HP is less than or equal to 0, then print death message
        print('You died')
        return player['HP']  # Return HP so combat_round function knows whether combat has ended
    else:
        print('You now have', player['HP'], 'HP')  # If you didn't die, then print remaining HP
        return player['HP']


def main():
    my_character = character.create_character()
    print("The X represents your current location. The O's represents available spaces to move into.")
    dungeon_map(0, 0, my_character)


if __name__ == "__main__":
    main()
