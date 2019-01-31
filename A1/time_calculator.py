"""Convert second to minutes, hours and days."""

# Jacky Zheng
# A01086998
# 01/30/19


def time_calculator(seconds):
    """Convert seconds to minutes, hours, and days.
    PARAM: seconds, a positive integer
    PRECONDITION: seconds must be a positive integer
    POSTCONDITION: converts seconds to minutes, hours, and days
    RETURN: a list that contains seconds and equivalent minutes, hours, and days."""
    seconds = int(seconds)
    minutes = seconds // 60
    hours = seconds // 3600
    days = seconds // 86400
    time_list = [days, hours, minutes, seconds]
    return time_list


def main():
    print(time_calculator(8000))


if __name__ == '__main__':
    main()

