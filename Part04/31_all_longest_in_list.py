# Write your solution here

def all_the_longest(lista):

    longest = lista[0]
    list_all_longest = []
    
    # primero se  busca la longitud de la palabra mas larga
    for word in lista:
        if len(word) > len(longest):
            longest = word

    len_longest = len(longest)    

    # se itera sobre toda la lista y se agrega solo las palabras 
    # que machean con el largo de la palabra mas larga 

    for word in lista:   
        if len(word) == len_longest:
            list_all_longest.append(word)

    return list_all_longest     


if __name__ == "__main__":

    main()