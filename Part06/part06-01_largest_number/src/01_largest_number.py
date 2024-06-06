def largest():

    with open("numbers.txt") as new_file:
        content = new_file.read()

    lista_numero_str = content.split() # transforma el str en una lista. Split usa el espacio para separar los numeros
    lista_numero_int = []
    
    for numero_str in lista_numero_str:
        numero = int(numero_str)
        lista_numero_int.append(numero)
        

    return max(lista_numero_int)    

if __name__ == "__main__":

    print(largest())
