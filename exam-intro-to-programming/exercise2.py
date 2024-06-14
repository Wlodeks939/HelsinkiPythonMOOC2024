def copy(matrix: list):

    copy_list = []
    for item_list in matrix:
        temp_item_list = item_list.copy()
        copy_list.append(temp_item_list)

    return copy_list    


def flip(matrix: list):

    for item_list in matrix:
        a = item_list[0]
        b = item_list[1]
        item_list[0] = b
        item_list[1] = a

    return None    


def flip_and_copy(matrix: list):

    matrix2 = copy(matrix)
    flip(matrix2)
        
    return matrix2

