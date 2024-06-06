from string import ascii_lowercase,digits,punctuation
from random import choice


def generate_strong_password(n: int,num: bool,special: bool):

    letras = ascii_lowercase
    numeros = digits
    especiales = "!?=+-()#"

    letrasynumeros = letras + numeros
    letrasyespeciales = letras + especiales
    letrasnumerosyespeciales = letras + numeros + especiales    

    # agrego una letra. La contrasena debe tener al menos una letra
    contrasena = ""
    contrasena += choice(letras)

    if num == True:
        contrasena += choice(numeros)
    if special == True:
        contrasena += choice(especiales)   

    longitud_actual = len(contrasena)     


    for i in range(n-longitud_actual):
        if num == False and special == False:
            contrasena += choice(letras)
        elif num == True and special == False:
            contrasena += choice(letrasynumeros)
        elif num == False and special == True:
            contrasena += choice(letrasyespeciales)
        elif num == True and special == True:
            contrasena += choice(letrasnumerosyespeciales)        


    return contrasena


if __name__ == "__main__":

    print(generate_strong_password(8,True,False))