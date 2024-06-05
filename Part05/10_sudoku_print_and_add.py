def print_sudoku(sudoku: list):

    col_ind = 0
    row_ind = 0


    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                sudoku[i][j] = "_"
            print(sudoku[i][j],end = " ")
            col_ind += 1
            if col_ind == 3:  # para separar cada 3 valores
                print(" ",end = "")
                col_ind = 0
        print("")  # salta la linea despues de cada fila  
        row_ind += 1
        if row_ind == 3:  # para separar cada 3 valores
                print("")
                row_ind = 0


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
     
    sudoku[row_no][column_no] = number


if __name__ == "__main__":


    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)    
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)    