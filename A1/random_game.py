"""Play a random game of rock, paper, scissors against the computer."""

# Jacky Zheng
# A01086998
# 01/30/19

import random  # Need to use the randint method
import doctest


def rock_paper_scissors():
    """Play a random game of rock, paper, scissors against the computer."
    PRECONDITION: user must input 'rock', 'paper', or 'scissors'
    POSTCONDITION: prints the results of the rock, paper, scissors match"""
    guess = input('rock, paper, or scissors?')
    guess = guess.lower()  # If the user capitalizes anything, turns input to lower case
    guess = guess.strip()  # Gets rid of any pesky white space
    if guess in ('rock', 'paper', 'scissors'):  # If the user correctly inputs a guess, the function will continue
        print(random_generator(guess))
    else:
        print('You did not type rock, paper, or scissors!')  # If the user does not correctly input, generates message


def random_generator(guess):
    """Generate a random integer and assign computer's choice to it."

    # Also passes guess into another function
    PARAM: guess, a string as 'rock', 'paper', or 'scissors'
    PRECONDITION: must be a string as 'rock', 'paper', or 'scissors'
    POSTCONDITION: assigns the computer's choice to the same random number and passes the computer's choice
    and the user's choice to the guess_computer function for comparison
    """
    generated = random.randint(0, 2)  # Generate a random integer in the range of [0, 2]
    if generated == 0:  # 0 will always be rock
        computer = 'rock'
    elif generated == 1:  # 1 will always be paper
        computer = 'paper'
    elif generated == 2:
        computer = 'scissors'  # 2 will always be scissors
    guess_vs_computer(guess, computer)  # Passes the two values to compare to the next function


def guess_vs_computer(guess, computer):
    """Compare the user's choice against the computer's choice and prints who won.

    PARAM: guess, a string as 'rock', 'paper', or 'scissors'
    PARAM: computer, a string as 'rock', 'paper', or 'scissors'
    PRECONDITION: guess must be a string as 'rock', 'paper', or 'scissors'
    PRECONDITION: computer must be a string as 'rock', 'paper', or 'scissors'
    POSTCONDITION: prints the winner of the rock, paper, scissors game
    >>> guess_vs_computer('rock', 'scissors')
    'Computer picked scissors. You win :)'
    >>> guess_vs_computer('paper', 'scissors')
    'Computer picked scissors. You lose :('
    >>> guess_vs_computer('rock', 'rock')
    'Computer picked the same. You tied :/'
    """
    if guess == computer:
        return 'Computer picked the same. You tied :/'
    elif guess == 'rock' and computer == 'scissors':
        return 'Computer picked scissors. You win :)'
    elif guess == 'rock' and computer == 'paper':
        return 'Computer picked paper. You lose :('
    elif guess == 'paper' and computer == 'rock':
        return 'Computer picked rock. You win :)'
    elif guess == 'paper' and computer == 'scissors':
        return 'Computer picked scissors. You lose :('
    elif guess == 'scissors' and computer == 'paper':
        return 'Computer picked paper. You win :)'
    elif guess == 'scissors' and computer == 'rock':
        return 'Computer picked rock. You lose :('


def main():
    """Drives the function."""
    rock_paper_scissors()
    doctest.testmod()


if __name__ == '__main__':
    main()
