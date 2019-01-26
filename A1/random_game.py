
import random


def rock_paper_scissors():
    guess = input('rock, paper, or scissors?')
    guess = guess.lower()
    guess = guess.strip()
    if guess in ('rock', 'paper', 'scissors'):
        random_generator(guess)
    else:
        print('You did not type rock, paper, or scissors!')


def random_generator(guess):
    generated = random.randint(0, 2)
    if generated == 0:
        computer = 'rock'
    elif generated == 1:
        computer = 'paper'
    elif generated == 2:
        computer = 'scissors'
    guess_vs_computer(guess, computer)


def guess_vs_computer(guess, computer):
    if guess == computer:
        print('Computer picked the same. You tied :/')
    elif guess == 'rock' and computer == 'scissors':
        print('Computer picked scissors. You win :)')
    elif guess == 'rock' and computer == 'paper':
        print('Computer picked paper. You lose :(')
    elif guess == 'paper' and computer == 'rock':
        print('Computer picked rock. You lose :(')
    elif guess == 'paper' and computer == 'scissors':
        print('Computer picked scissors. You lose :(')
    elif guess == 'scissors' and computer == 'paper':
        print('Computer picked paper. You win :)')
    elif guess == 'scissors' and computer == 'rock':
        print('Computer picked rock. You lose :(')


def main():
    rock_paper_scissors()


if __name__ == '__main__':
    main()
