from fractions import *

def fractionate(amount: int):

    lista = []

    for i in range(amount):
        lista.append(Fraction(1,amount))

    return lista


if __name__ == "__main__":
    print(fractionate(5))