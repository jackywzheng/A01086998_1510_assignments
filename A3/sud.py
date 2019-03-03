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


def dungeon_map(horizontal, vertical):
    dungeon = [['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'X', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O'],
               ['O', 'O', 'O', 'O', 'O']]
    dungeon[2+horizontal][2+vertical] = 'X'
    for row in dungeon:
        for column in row:
            print(column, end=' ')  # Print
        print()


def movement_input():
    direction = input("Which direction do you want to travel? Type 'n' for North, 'e' for East, "
                      "'w' for West, 's' for South. Type 'quit' to quit playing.")
    direction.lower().strip()
    if direction == 'n':
        dungeon_map(-1, 0)
    elif direction == 'e':
        dungeon_map(0, 1)
    elif direction == 'w':
        dungeon_map(0, -1)
    elif direction == 's':
        dungeon_map(1, 0)
    elif direction == 'quit':
        pass
    else:
        print("That was not a valid input. Please enter a valid input.")
        movement_input()


def combat_choice(player, enemy):
    choice = input("Do you wish to fight the monster? Type 'yes' to fight. Type 'no' to flee.")
    choice.lower().strip()
    if choice == 'yes':  # If player chooses to fight, execute combat_round function
        combat_round(player, enemy)
    elif choice == 'no':  # If player chooses to flee, roll a 1d10 to represent a 10% chance
        chance = roll_die(1, 10)
        if chance == 5:  # If it lands on a 5, player takes 1d4 damage
            player["HP"] -= roll_die(1, 4)
    else:
        print("You did not type a valid input. Type 'yes' or 'no'.")
        combat_choice(player, enemy)  # Call the function again if player typed something else


def combat_round(player, enemy):
    first_attack = roll_die(1, 2)  # Roll a 1d2, represents 50% chance of either character or enemy attacking first
    if first_attack == 1:  # If it's a 1, player attacks first
        print('You attack first')
        player_attack(enemy)
    else:  # If it's a 2, enemy attacks first
        print('Enemy attacks first')
        enemy_attack(player)


def player_attack(enemy):
    damage = roll_die(1, 6)  # Roll corresponding 1d6 to determine damage
    print('You did', damage, 'damage')
    enemy['HP'] -= damage  # Replace enemy's HP value with the difference
    if enemy['HP'] <= 0:  # If the HP is less than or equal to 0, then print death message
        print('Enemy has died')
        return enemy['HP']  # Return HP so combat_round function knows whether combat has ended
    else:
        print('Enemy now has', enemy['HP'], 'HP')  # If enemy didn't die, then print remaining HP


def enemy_attack(player):
    damage = roll_die(1, 6)  # Roll corresponding 1d6 to determine damage
    print('Enemy did', damage, 'damage')
    player['HP'] -= damage  # Replace character's HP value with the difference
    if player['HP'] <= 0:  # If the HP is less than or equal to 0, then print death message
        print('You died')
        return player['HP']  # Return HP so combat_round function knows whether combat has ended
    else:
        print('Enemy now has', player['HP'], 'HP')  # If you didn't die, then print remaining HP


def main():
    movement_input()


if __name__ == "__main__":
    main()
