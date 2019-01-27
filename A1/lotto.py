import random


def number_generator():
    lottery = list(range(1, 49))
    lottery = random.sample(lottery, 6)
    print(sorted(lottery))


def main():
    number_generator()


if __name__ == '__main__':
    main()
