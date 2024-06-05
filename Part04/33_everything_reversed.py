# Write your solution here


def everything_reversed(lista):

    lista2 = []
    for word in lista:
        
        word2 = word[::-1]
        lista2.append(word2)

    lista3 = lista2[::-1]


    return lista3



if __name__ == "__main__":

    lista = ["Hi", "there", "example", "one more"]

    print(everything_reversed(lista))