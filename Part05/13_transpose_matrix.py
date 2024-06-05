def transpose(matrix: list):

    n = len(matrix[0])

    
    for i in range(n-1):  # 0,1   no hace falta la fila 2 porque ya esta transpuesta
        for j in range(i+1, n):  # 1er bucle 1,2  #2do bucle 2
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


if __name__ == "__main__":
    matrix1 = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    print(matrix1)  

  