def read_file(filename):

    with open(filename) as file:
        content = file.read()

    # creacion lista de strings. Cada string es una receta. 
    lista_str = content.split("\n\n") # ['Pancakes\n15\nmilk\neggs\nflour\nsugar\nsalt\nbutter', 'Meatballs
                                     
    # creacion lista de listas. Cada lista es una receta. tiempo es tipo string
    lista_recetas = [] # [['Pancakes', '15', 'milk', 'eggs', 'flour', 'sugar', 'salt', 'butter'], ['Meatballs
    
    for string in lista_str:
        lista = string.split("\n")
        lista_recetas.append(lista)

    for lista in lista_recetas:  # transformamos el tiempo de string a int
        temp = lista[1]
        lista[1] = int(temp) 

    return lista_recetas

def search_by_name(filename: str, word: str):

    lista_recetas = read_file(filename)
    # crea una lista con las recetas que matchean con la palabra ingresada en la funcion
    lista_matches = []  
    for receta in lista_recetas:
        if word in receta[0].lower():
            lista_matches.append(receta[0])  

    return lista_matches

def search_by_time(filename: str, prep_time: int):

    lista_recetas = read_file(filename)
    # crea una lista con las recetas que matchean con la palabra ingresada en la funcion 
    lista_matches = []  
    for receta in lista_recetas:
        if receta[1] < prep_time:
            elemento = f"{receta[0]}, preparation time {receta[1]} min"
            lista_matches.append(elemento) 

    return lista_matches   

def search_by_ingredient(filename: str, ingredient: str):

    lista_recetas = read_file(filename)
    # crea una lista con las recetas que matchean con la palabra ingresada en la funcion
    lista_matches = []  
    for receta in lista_recetas:
        if ingredient in receta:
            elemento = f"{receta[0]}, preparation time {receta[1]} min"
            lista_matches.append(elemento) 

    return lista_matches 
   
if __name__ == "__main__":

    #print(search_by_name("recipes1.txt", "cake"))
    #print(search_by_time("recipes1.txt", 20))
    print(search_by_ingredient("recipes1.txt", "eggs"))