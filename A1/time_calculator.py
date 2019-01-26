def time_calculator(seconds):
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

