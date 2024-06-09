
def add_numbers_to_list(numbers: list):

    if len(numbers) % 5 != 0:
        temp = numbers[-1] + 1
        numbers.append(temp)
        add_numbers_to_list(numbers)


