def row_sums(my_matrix: list):

    for lista in my_matrix:
        suma = 0
        for num in lista:
            suma += num

        lista.append(suma)


if __name__ == "__main__":

    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)