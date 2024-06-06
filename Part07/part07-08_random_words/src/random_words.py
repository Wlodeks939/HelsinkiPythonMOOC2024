from random import *


def words(n: int, beginning: str):

    with open("words.txt") as file:
        lista_str = file.read().split("\n") # ['a', 'aah', 'aahed', 'aahing', 'aahs', ...

    lista_match = []
    for str in lista_str:
        if str.startswith(beginning) and str not in lista_match:
            lista_match.append(str)

    if len(lista_match) < n:
        raise ValueError("ValueError exception")


    lista_final = []

    while len(lista_final) < n:
        temp = choice(lista_match)
        if temp not in lista_final:
            lista_final.append(temp)

    return lista_final
  

if __name__ == "__main__":
    print(words(5,"engine"))