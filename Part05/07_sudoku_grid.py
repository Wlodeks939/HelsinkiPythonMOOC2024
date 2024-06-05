def row_correct(sudoku: list, row_no: int):

    # arma una lista con los numeros de la fila dada
    row_sorted = []
    for num in sudoku[row_no]:
        row_sorted.append(num)

    # ordena la lista. La lista ordenada nos sirve para encontrar duplicados
    row_sorted = sorted(row_sorted)

    # recorre la lista ordenada comparando adyacentes para encontrar duplicados
    for i in range(len(row_sorted)-1):
        if row_sorted[i] == row_sorted[i+1] and row_sorted[i] != 0:
            return False
        
    return True


def column_correct(sudoku: list, column_no: int):

    col_sorted = []

    #arma una lista de numeros. Para cada fila solo agrega la columna dada
    for row in sudoku:
        col_sorted.append(row[column_no])

    col_sorted = sorted(col_sorted)

    # recorre la lista ordenada comparando adyacentes para encontrar duplicados
    for i in range(len(col_sorted)-1):
        if col_sorted[i] == col_sorted[i+1] and col_sorted[i] != 0:
            return False
        
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):

    block_sorted = []

    # arma una lista de numeros traversando el bloque de 3x3
    for i in range(len(sudoku[row_no:row_no+3])):
        for j in range(len(sudoku[column_no:column_no+3])):
            block_sorted.append(sudoku[i+row_no][j+column_no])


    block_sorted = sorted(block_sorted)  

    # recorre la lista ordenada comparando adyacentes para encontrar duplicados
    for i in range(len(block_sorted)-1):
        if block_sorted[i] == block_sorted[i+1] and block_sorted[i] != 0:
            return False
        
    return True


def sudoku_grid_correct(sudoku: list):

    # chequeo filas
    for i in range(9):
        if not row_correct(sudoku, i):
            return False
      
    # chequeo columnas
    for i in range(9):
        if not column_correct(sudoku, i):
            return False
    
    
    # chequeo bloques
    lista_filas = [0,3,6]
    lista_col = [0,3,6]

    for i in range(3):
        for j in range(3):
            if not block_correct(sudoku,lista_filas[i],lista_col[j]):
                return False


    return True        

   
    



