# Write your solution here


def formatted(lista):

    lista2 = []

    for num in lista:
        num2 = f"{num:.2f}"
        lista2.append(num2)

    return lista2

#lista = [1.2, 0.3333, 0.11111, 3.446]

#print(formatted(lista))



if __name__ == "__main__":

    main()