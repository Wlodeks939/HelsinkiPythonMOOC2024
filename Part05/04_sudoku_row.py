def row_correct(sudoku: list, row_no: int):

    row_sorted = []
    for num in sudoku[row_no]:
        row_sorted.append(num)

    row_sorted = sorted(row_sorted)

    for i in range(len(row_sorted)-1):
        if row_sorted[i] == row_sorted[i+1] and row_sorted[i] != 0:
            return False
        
    return True
        

