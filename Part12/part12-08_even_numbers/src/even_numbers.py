def even_numbers(beginning: int, maximum: int):

    if beginning % 2 == 0:
        primer_num = beginning
    else:
        primer_num = beginning + 1

    if maximum % 2 == 0:
        ultimo_num = maximum
    else:
        ultimo_num = maximum - 1

    while primer_num <= ultimo_num:
        yield primer_num
        primer_num += 2            


numbers = even_numbers(11, 21)
for number in numbers:
    print(number)


