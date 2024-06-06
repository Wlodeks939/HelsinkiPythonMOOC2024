def matrix_max():

    with open("matrix.txt") as file:
        content = file.read()

    lista_str = content.split()
    lista_num = []

    for linea in lista_str:
        x = linea.split(",")
        for num_str in x:
            lista_num.append(int(num_str))

    return max(lista_num)


def matrix_sum():

    with open("matrix.txt") as file:
        content = file.read()

    lista_str = content.split()
    lista_num = []

    for linea in lista_str:
        x = linea.split(",")
        for num_str in x:
            lista_num.append(int(num_str))

    suma = 0
    for num in lista_num:
        suma += num
    return suma


def row_sums():

    with open("matrix.txt") as file:
        content = file.read()

    lista_str = content.split()

    lista_suma_row = []
   
    for j in range(len(lista_str)):
        lista = lista_str[j].split(",")
        suma = 0
        for num in lista:
            suma += int(num)
        lista_suma_row.append(suma)    

    
    return lista_suma_row

if __name__ == "__main__":
    row_sums()

    