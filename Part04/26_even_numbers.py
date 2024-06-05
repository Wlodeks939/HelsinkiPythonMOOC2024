# Write your solution here

def even_numbers(lista):

    lista_par = []

    for num in lista:
        if num % 2 == 0:
            lista_par.append(num)

    return lista_par        
