# Write your solution here

def length_of_longest(lista):

    longest = lista[0]
    

    for word in lista:
        if len(word) > len(longest):
            longest = word

    return len(longest)        


if __name__ == "__main__":

    main()