def selection_sort(a_list):
    if type(a_list) is not list or len(a_list) == 0:
        raise ValueError("a_list must be a list and not empty!")
    index = 0
    length = len(a_list)
    while index < length:
        b_list = a_list.copy()
        lowest = 0
        for i in range(index, length):
            if a_list[i] < b_list[index]:
                lowest = i  # Finds index with lowest number
        a_list[index] = b_list[lowest]
        a_list[lowest] = b_list[index]
        index += 1
        print(a_list)
        print(b_list)
        print(index)
        print(lowest)



selection_sort([3, 5, 1, 9, -4])