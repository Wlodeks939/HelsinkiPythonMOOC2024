from string import *
from random import *


def generate_password(n):

    letras = ascii_lowercase
    lista_contrasena = sample(letras, n)

    contrasena2 = ""

    for letra in lista_contrasena:
        contrasena2 += letra

    return contrasena2


if __name__ == "__main__":

    print(generate_password(5))

