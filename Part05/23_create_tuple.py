def create_tuple(x: int, y: int, z: int):

    lista = [x,y,z]

    mini = min(lista)
    maximo = max(lista)
    suma = x + y + z
    tupla = (mini,maximo,suma)

    return tupla


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))