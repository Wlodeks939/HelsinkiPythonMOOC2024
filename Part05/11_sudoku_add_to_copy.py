def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):


    sudoku2  = [
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
    # copia el sudoku
    for i in range(9):
         for j in range(9):
              sudoku2[i][j] == sudoku[i][j]

    # agrega numero

    sudoku2[row_no][column_no] = number                  

    return sudoku2



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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)                

 