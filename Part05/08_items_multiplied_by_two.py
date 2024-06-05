def double_items(numbers: list):

    new_list = numbers[:]

    for i in range(len(new_list)):
        new_list[i] = new_list[i] * 2

    return new_list    