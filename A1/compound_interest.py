def compound_interest(p, r, n, t):
    a = p * (1 + r / n) ** (n * t)
    return a


def main():
    compound_interest(50000, 0.1, 2, 10)


if __name__ == '__main__':
    main()
