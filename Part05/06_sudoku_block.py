def block_correct(sudoku: list, row_no: int, column_no: int):

    block_sorted = []

    for i in range(len(sudoku[row_no:row_no+3])):
        for j in range(len(sudoku[column_no:column_no+3])):
            block_sorted.append(sudoku[i+row_no][j+column_no])


    block_sorted = sorted(block_sorted)  

    for i in range(len(block_sorted)-1):
        if block_sorted[i] == block_sorted[i+1] and block_sorted[i] != 0:
            return False
        
    return True

