def read_fruits():

    with open("fruits.csv") as file:
        content = file.read()

    lista_str = content.split()
   

    d = {}
    for item in lista_str:
        key,value = item.split(";")
        d[key] = float(value)

    return d

if __name__ == "__main__":

    read_fruits()