# Write your solution here


def distinct_numbers(lista):

    lista_sorted = sorted(lista)

    n = int(len(lista))

    lista2 = []
    lista2.append(lista_sorted[0])

    for i in range(n-1):
        if lista_sorted[i+1] != lista_sorted[i]:
            lista2.append(lista_sorted[i+1])

   


    return lista2


   
if __name__ == "__main__":

    main()
   
        

