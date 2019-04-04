from math import sqrt


def sum_of_primes(upperbound):
    sieve = list(range(upperbound))
    sieve_copy = list(range(2, upperbound))
    if upperbound < 0:
        raise ValueError("upperbound must be a positive integer!")
    for number in sieve_copy:
        if number > int(sqrt(upperbound)):
            print(number)
            break
        for num in range(2, int(sqrt(upperbound)) + 1):
            if number % num != 0:  # Prime
                for i in range(2, int(upperbound/2)):
                    try:
                        sieve.remove(number * i)
                    except ValueError:
                        continue
    print(sieve)
    return sum(sieve)

