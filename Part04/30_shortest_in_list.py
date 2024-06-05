# Write your solution here


def shortest(lista):

    short = lista[0]
    

    for word in lista:
        if len(word) < len(short):
            short = word

    return short    


if __name__ == "__main__":

    main()