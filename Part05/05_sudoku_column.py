def column_correct(sudoku: list, column_no: int):

    col_sorted = []
    for row in sudoku:
        col_sorted.append(row[column_no])

    col_sorted = sorted(col_sorted)

  

    for i in range(len(col_sorted)-1):
        if col_sorted[i] == col_sorted[i+1] and col_sorted[i] != 0:
            return False
        
    return True


