def times_ten(start_index: int, end_index: int):

    d = {}

    for i in range(start_index,end_index+1):
        d[i] = int(i) * 10

    return d    